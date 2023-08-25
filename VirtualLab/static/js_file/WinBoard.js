var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.querySelectorAll(".slideshow-container .mySlides");

    for (i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
    }

    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1
    }
    slides[slideIndex - 1].classList.add("active");

    setTimeout(showSlides, 5000);
}

function plusSlides(n) {

    slideIndex += n;
    
    var slides = document.querySelectorAll(".slideshow-container .mySlides");
    for (var i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
    }

    if (slideIndex < 1) {
        slideIndex = slides.length;
    } else if (slideIndex > slides.length) {
        slideIndex = 1;
    }

    slides[slideIndex - 1].classList.add("active");
}
