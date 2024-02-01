var link = document.querySelector('#menu_trigger');
var elem = document.querySelector('#menu');

link.addEventListener('click', function () {
    elem.classList.toggle('show')
});