const header = document.querySelector(".header");
const menuBtn = document.querySelector("#menu-btn");

window.addEventListener("scroll", (e) => {
    const scroll = window.scrollY;
    if (scroll > 100) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
})