let idkk= true;

function am() {
    document.querySelector('.amin').classList.toggle('vad');
    if (a) {
        document.querySelector("#but").innerHTML = `<lord-icon
                        src="https://cdn.lordicon.com/rivoakkk.json"
                        trigger="loop"
                        colors="primary:#0e121b,secondary:#edf5e1"
                        stroke="76"
                        style="width:70px;height:70px">
                    </lord-icon>`;
        idkk= false;
    } else {
        document.querySelector("#but").innerHTML = `<lord-icon src="https://cdn.lordicon.com/rhvddzym.json" trigger="loop"
                        colors="primary:#edf5e1,secondary:#08a88a" stroke="76" style="width:70px;height:70px">
                    </lord-icon>`;
        idkk= true;
    }
}
var swiper = new Swiper('.blog-slider', {
    spaceBetween: 30,
    effect: 'fade',
    loop: true,
    autoHeight: false,
    pagination: {
        el: '.blog-slider__pagination',
        clickable: true,
    }
});


$('#mess').on('focus', () => {
    $('*').addClass('password');
}).on('focusout', () => {
    $('*').removeClass('password');
});;




const option = document.querySelectorAll(".option");

for (let i = 0; i < option.length; i++) {
    option[i].addEventListener("click", () => {
        if (!option[i].classList.contains("active")) {
            closeAll();
            option[i].classList.add("active");
        } else {
            option[i].classList.remove("active");
        }
    });
}

function closeAll() {
    for (let i = 0; i < option.length; i++) {
        if (option[i].classList.contains("active")) {
            option[i].classList.remove("active");
        }
    }
}
 

const sc = document.querySelector("#sc");
const an = document.querySelector("#an");

window.addEventListener("scroll", (e) => {
    const scroll = window.scrollY;

    an.style.top = scroll / -2.5 + 700 + 132.8 + "px";

    document.querySelector("#bcc5b269-2c15-4ceb-87ee-2336ac482635").style.top = scroll / -4 + 0 +
        "px";
    document.querySelector("#txtB").style.top = scroll / -6 + 0 +
        "px";
    if (window.innerWidth <= 767) {
        document.querySelector(".ilu").style.top = scroll / -7 + 270 + "px";
    } else {
        document.querySelector(".ilu").style.top = scroll / -2 + 660 + "px";
    }

    const ben = document.querySelectorAll(".ben");

    for (let i = 0; i < ben.length; i++) {
        ben[i].style.top = scroll / -i / 10 + 2 + 62.1 + "px";
    }
});

var logoElement = $('footer .logo');

$(window).scroll(function () {

    if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {

        $(logoElement).addClass('show');

    } else if ($(logoElement).hasClass('show') && $(window).scrollTop() + $(window).height() > $(
            document).height() - 150) {

        $(logoElement).removeClass('show');

    }
});
const button = document.querySelector("#button");
const sageata = document.querySelector("#sageata");
// const sageata = window.getComputedStyle(
//     document.querySelector('#sageata'), ':before'
// );
const hide = document.querySelector(".hide");

function more() {
    if (button.classList.contains("a")) {
        sageata.classList.remove("fa-chevron-down");
        sageata.classList.add("fa-chevron-right");
        // sageata.style.transform = "rotateZ(0deg)";
        hide.style.height = "0";
        button.classList.remove("a");
    } else {
        // sageata.style.transform = "rotateZ(90deg)";

        sageata.classList.remove("fa-chevron-right");
        sageata.classList.add("fa-chevron-down");

        hide.style.height = "auto";
        button.classList.add("a");
    }
}

