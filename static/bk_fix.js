/* Burnt Kingdoms WW2 - Telegram initData recovery */
(function () {
  'use strict';
  var KEY = 'bk_tg_init';

  function fromParams(raw) {
    try {
      var params = new URLSearchParams(String(raw || '').replace(/^[?#]/, ''));
      return params.get('tgWebAppData') || '';
    } catch (e) { return ''; }
  }
  function fromHash() { return fromParams(location.hash); }
  function fromSearch() { return fromParams(location.search); }
  function stored() {
    try { return sessionStorage.getItem(KEY) || ''; } catch (e) { return ''; }
  }
  function save(value) {
    try { if (value) sessionStorage.setItem(KEY, value); } catch (e) {}
  }
  function getInitData() {
    var value = '';
    try {
      value = String(window.Telegram && window.Telegram.WebApp &&
        window.Telegram.WebApp.initData || '').trim();
    } catch (e) {}
    if (!value) value = fromHash();
    if (!value) value = fromSearch();
    if (!value) value = stored();
    if (value) save(value);
    return value;
  }

  window.__bkInitData = getInitData;
  var initialData = getInitData();

  // Some Telegram clients expose launch data before the WebApp bridge object is
  // ready. Provide the small interface this app uses, without bypassing server
  // signature validation. A real WebApp object is never replaced.
  try {
    if (!window.Telegram) window.Telegram = {};
    if (!window.Telegram.WebApp) {
      window.Telegram.WebApp = {
        initData: initialData,
        ready: function () {},
        expand: function () {},
        enableClosingConfirmation: function () {}
      };
    } else if (!window.Telegram.WebApp.initData && initialData) {
      window.Telegram.WebApp.initData = initialData;
    }
  } catch (e) {}

  var overlay = null;
  function showProblem() {
    if (overlay || !document.body) return;
    overlay = document.createElement('div');
    overlay.setAttribute('dir', 'rtl');
    overlay.style.cssText = 'position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.88);color:#fff;display:flex;align-items:center;justify-content:center;padding:24px;text-align:center;font:16px/1.9 sans-serif';
    overlay.innerHTML = '<div style="max-width:420px"><div style="font-size:20px;margin-bottom:10px">ورود تلگرام تأیید نشد</div>' +
      '<div style="opacity:.9">لطفاً بازی را دوباره از داخل ربات و با دکمهٔ ورود باز کنید.</div>' +
      '<button id="bk-retry" style="margin-top:16px;padding:10px 22px;border:0;border-radius:8px;font-size:15px">تلاش دوباره</button></div>';
    document.body.appendChild(overlay);
    var button = document.getElementById('bk-retry');
    if (button) button.onclick = function () { location.reload(); };
  }
  function hideProblem() {
    if (overlay && overlay.parentNode) overlay.parentNode.removeChild(overlay);
    overlay = null;
  }

  var originalFetch = window.fetch;
  window.fetch = function (input, init) {
    var url = typeof input === 'string' ? input : ((input && input.url) || '');
    var isGameApi = /\/api\//.test(url) && !/\/api\/catalog(?:\?|$)/.test(url);
    if (isGameApi && init && typeof init.body === 'string') {
      try {
        var body = JSON.parse(init.body);
        if (!body.init) {
          body.init = getInitData();
          init = Object.assign({}, init, { body: JSON.stringify(body) });
        }
      } catch (e) {}
    }
    var request = originalFetch.call(this, input, init);
    if (!isGameApi) return request;
    return request.then(function (response) {
      try {
        if (response.status === 401) {
          if (document.body) showProblem();
          else document.addEventListener('DOMContentLoaded', showProblem, { once: true });
        } else if (response.ok) {
          hideProblem();
        }
      } catch (e) {}
      return response;
    });
  };
})();