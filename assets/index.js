'use strict';

window.generateSecretKeys = (function () {
  return function _generateSecretKeys() {
    _getSecretKeysRequest(_listener);
  };

  function _listener() {
    var _secretKeysDiv = document.querySelector('.secret-keys');
    var _inputs = _secretKeysDiv.children;

    var object = {
      secretKeysDiv: _secretKeysDiv,
      inputs: _inputs,
    };

    if (this.status === 200) {
      var secretKeys = JSON.parse(this.responseText);

      if (_inputs.length === 0) {
        _addInputs.call(object, secretKeys);
      } else {
        _replaceInputs.call(object, secretKeys);
      }
    }
  }

  function _getSecretKeysRequest(listener) {
    var xhr = new XMLHttpRequest();
    xhr.onload = listener;
    xhr.open('get', '/api/secret_keys/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
  }

  function _getInputElement(value) {
    var input = document.createElement('input');
    input.value = value;
    input.size = 60;
    input.style.setProperty('text-align', 'center');
    return input
  }

  function _addInputs(list) {
    for (var i = 0; i < list.length; i++) {
      var input = _getInputElement(list[i]);
      this.secretKeysDiv.appendChild(input);
    }
  }

  function _replaceInputs(list) {
    for (var i = 0; i < list.length; i++) {
      var input = _getInputElement(list[i]);
      this.secretKeysDiv.replaceChild(input, this.inputs[i]);
    }
  }
})();
