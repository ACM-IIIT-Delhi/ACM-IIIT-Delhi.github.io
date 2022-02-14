function toggleNavbar(collapseID) {
    document.getElementById(collapseID).classList.toggle("hidden");
    document.getElementById(collapseID).classList.toggle("block");
}

/* Progress bar */
//Source: https://alligator.io/js/progress-bar-javascript-css-variables/
var h = document.documentElement,
    b = document.body,
    st = 'scrollTop',
    sh = 'scrollHeight',
    progress = document.querySelector('#progress'),
    scroll;
var scrollpos = window.scrollY;
var header = document.getElementById("header");
// console.log(document.body.clientHeight);

document.addEventListener('scroll', function () {
    var navImageHeight = Math.max(h.clientHeight || 0, window.innerHeight || 0) * 0.75;
    var footerHeight = document.getElementById('footer').clientHeight;
    /*Refresh scroll % width*/
    scroll = (h[st] || b[st]) / ((h[sh] || b[sh]) - navImageHeight - footerHeight) * 100;
    progress.style.setProperty('--scroll', scroll + '%');

    /*Apply classes for slide in bar*/
    scrollpos = window.scrollY;
    // console.log(scrollpos);
    if (scrollpos > navImageHeight) {
        header.classList.remove("hidden");
        header.classList.remove("fadeOutUp");
        header.classList.add("slideInDown");
    }
    else {
        header.classList.remove("slideInDown");
        header.classList.add("fadeOutUp");
        header.classList.add("hidden");
    }

});