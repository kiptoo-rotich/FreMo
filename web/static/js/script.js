var items = document.getElementsByClassName("fade-item");
for (let i = 0; i < items.length; ++i) {
    fadeIn(items[i], i * 1000)
}

function fadeIn(item, delay) {
    setTimeout(() => {
        item.classList.add('fadein')
    }, delay)
}

var i = 0;
var txt = 'A beautiful Birth Centre that Advocates and facilitates Normal Births. Compassion, Gentleness and Social Justice.'; /* The text */
var speed = 50; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("typing").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}
typeWriter()


$('#recipeCarousel').carousel({
    interval: 2000
})

$('.carousel .carousel-item').each(function() {
    var next = $(this).next();
    if (!next.length) {
        next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));

    for (var i = 0; i < 2; i++) {
        next = next.next();
        if (!next.length) {
            next = $(this).siblings(':first');
        }

        next.children(':first-child').clone().appendTo($(this));
    }
});

$('.carousel').carousel({
    interval: 1000
})