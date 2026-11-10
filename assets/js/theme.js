(function () {
  'use strict';

  var storageKey = 'jun-yao-theme';
  var root = document.documentElement;
  var theme = 'light';
  var button;

  try {
    if (window.localStorage.getItem(storageKey) === 'dark') theme = 'dark';
  } catch (error) {
    // The switch still works when browser storage is unavailable.
  }
  root.setAttribute('data-theme', theme);

  function applyTheme(nextTheme) {
    theme = nextTheme === 'dark' ? 'dark' : 'light';
    root.setAttribute('data-theme', theme);
    button.setAttribute('aria-pressed', String(theme === 'dark'));
    button.setAttribute('title', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    var browserColor = document.querySelector('meta[name="theme-color"]');
    if (browserColor) browserColor.setAttribute('content', theme === 'dark' ? '#1c2029' : '#ffffff');
  }

  document.addEventListener('DOMContentLoaded', function () {
    button = document.querySelector('.theme-toggle');
    if (!button) return;
    applyTheme(theme);
    button.hidden = false;

    button.addEventListener('click', function () {
      applyTheme(theme === 'dark' ? 'light' : 'dark');
      try {
        window.localStorage.setItem(storageKey, theme);
      } catch (error) {
        // Keep the chosen theme for this page even without persistence.
      }
    });

    window.addEventListener('storage', function (event) {
      if (event.key === storageKey || event.key === null) applyTheme(event.newValue);
    });
  });
}());
