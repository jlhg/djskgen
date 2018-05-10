'use strict';

window.generateSecretKey = (function () {
  return function _generateSecretKeys() {
    _getSecretKeysRequest(_listener);
  };

  function _listener() {
    var _secretKeyWrapper = document.querySelector('.secret-key');

    if (this.status === 200) {
      /**
       * @type {{secretKey}}
       */
      var camelCaseResponse = _objectAttrsToCamelCase(JSON.parse(this.responseText));
      _secretKeyWrapper.querySelector('input').value = '\'' + camelCaseResponse.secretKey + '\'';
    }
  }

  function _getSecretKeysRequest(listener) {
    var xhr = new XMLHttpRequest();
    xhr.onload = listener;
    xhr.open('get', '/api/secret_key/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
  }

  function _objectAttrsToCamelCase(object) {
    var _object = {};

    for (var key in object) {
      if (object.hasOwnProperty(key)) {
        var camelCaseKey = key.replace(/_([a-z])/g, _innerToUpperCase);
        _object[camelCaseKey] = object[key];
      }
    }

    return _object;
  }

  function _innerToUpperCase(_, char) {
    return char.toUpperCase();
  }
})();

window.copySecretKey = (function () {
  return function _copySecretKey() {
    var input = document.querySelector('.secret-key input');
    input.select();
    if (document.queryCommandSupported('copy')) {
      document.execCommand('copy');
      window.showToaster('Secret key copied to your clipboard!');
    }
  }
})();
