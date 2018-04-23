'use strict';

var gtag = (function () {
  var gaId = _getParams('googleAnalytics')['id'];
  _loadGoogleAnalytics(gaId);

  window.dataLayer = window.dataLayer || [
    ['js', new Date()],
    ['config', gaId],
  ];

  return function _gtag() {
    dataLayer.push(arguments);
  };

  function _loadGoogleAnalytics(googleAnalyticsId) {
    var script = document.createElement('script');
    script.src = '//www.googletagmanager.com/gtag/js?id=' + googleAnalyticsId;
    document.head.appendChild(script);
  }

  function _getParams(script_name) {
    var scripts = document.getElementsByTagName("script");

    for (var i = 0; i < scripts.length; i++) {
      var regexp = new RegExp('/' + script_name + '.js');
      var src = scripts[i].src;

      if (regexp.test(src)) {
        var queryParams = src.split('?')[1].split('&');
        return queryParams.reduce(_parseParams, {});
      }
    }

    return {};
  }

  function _parseParams(params, value) {
    var keyValue = value.split('=');
    var _params = JSON.parse(JSON.stringify(params)); // Make a copy of params
    _params[keyValue[0]] = keyValue[1];
    return _params
  }
})();
