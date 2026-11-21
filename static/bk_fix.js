/* Burnt Kingdoms WW2 - Telegram initData recovery (put this file in static/bk_fix.js) */
(function () {
  'use strict';
  var KEY = 'bk_tg_init';

  function fromHash() {
    try {
      var raw = String(location.hash || '').replace(/^#/, '');
      return new URLSearchParams(raw).get('tgWebAppData') || '';
    } catch (e) { return ''; }
  }
  function fromSearch() {
    try { return new URLSearchParams(location.search).get('tgWebAppData') || ''; } catch (e) { return ''; }
  }
  function stored() { try { return sessionStorage.getItem(KEY) || ''; } catch (e) { return ''; } }
  function save(v) { try { if (v) sessionStorage.setItem(KEY, v); } catch (e) {} }

  function getInitData() {
    var v = '';
    try { v = (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.initData) || ''; } catch (e) {}
    if (!v) v = fromHash();
    if (!v) v = fromSearch();
    if (v) { save(v); return v; }
    return stored();
  }
  window.__bkInitData = getInitData;
  getInitData(); // capture as early as possible

  var box = null;
  function showProblem() {
    if (box || !document.body) return;
    box = document.createElement('div');
    box.setAttribute('dir', 'rtl');
    box.style.cssText = 'position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.88);color:#fff;display:flex;align-items:center;justify-content:center;padding:24px;text-align:center;font:16px/1.9 sans-serif';
    box.innerHTML = '<div style="max-width:420px"><div style="font-size:20px;margin-bottom:10px">ورود تلگرام تأیید نشد</div>' +
      '<div style="opacity:.9">لطفاً بازی را دوباره از داخل ربات و با دکمهٔ «ورود به کارزار جهانی دوم» باز کنید. اگر مشکل ادامه داشت، تلگرام را به‌روزرسانی کنید.</div>' +
      '<button id="bk-retry" style="margin-top:16px;padding:10px 22px;border:0;border-radius:8px;font-size:15px">تلاش دوباره</button></div>';
    document.body.appendChild(box);
    var b = document.getElementById('bk-retry');
    if (b) b.onclick = function () { location.reload(); };
  }
  function hideProblem() { if (box && box.parentNode) box.parentNode.removeChild(box); box = null; }

  var origFetch = window.fetch;
  window.fetch = function (input, init) {
    var url = typeof input === 'string' ? input : ((input && input.url) || '');
    var isGameApi = /\/api\//.test(url) && !/\/api\/catalog/.test(url);
    if (isGameApi && init && typeof init.body === 'string') {
      try {
        var body = JSON.parse(init.body);
        if (!body.init) {
          body.init = getInitData();
          init = Object.assign({}, init, { body: JSON.stringify(body) });
        }
      } catch (e) {}
    }
    var p = origFetch.call(this, input, init);
    if (!isGameApi) return p;
    return p.then(function (res) {
      try {
        if (res.status === 401) {
          if (document.body) showProblem(); else document.addEventListener('DOMContentLoaded', showProblem);
        } else if (res.ok) {
          hideProblem();
        }
      } catch (e) {}
      return res;
    });
  };
})();