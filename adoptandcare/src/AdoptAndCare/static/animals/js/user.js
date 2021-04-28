const max = 2;
const ar = document.querySelectorAll(".links .h4");
const opt = document.querySelectorAll(".info .opt");
for (let i = 0; i < max; i++) {
    ar[i].addEventListener("click", () => {
        for (let j = 0; j < max; j++) {
            opt[j].classList.remove("act");
        }
        opt[i].classList.toggle("act");
    });
}
