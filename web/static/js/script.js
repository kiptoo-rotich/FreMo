$('.carousel').carousel({
    interval: 2000
})

var items = document.getElementsByClassName("fade-item");
for (let i = 0; i < items.length; ++i) {
    fadeIn(items[i], i * 1000)
}

function fadeIn(item, delay) {
    setTimeout(() => {
        item.classList.add('fadein')
    }, delay)
}