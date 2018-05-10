// https://www.w3schools.com/howto/howto_js_snackbar.asp

window.showToaster = (function () {
  return function _showToaster(message) {
    var toaster = document.querySelector('.toaster');

    if (/show/.test(toaster.classList)) {
      return
    }

    toaster.innerText = message;
    toaster.className += ' show';

    setTimeout(function _hideToaster() {
      toaster.innerText = message;
      toaster.className = toaster.className.replace(' show', '');
    }, 3000);
  }
})();
