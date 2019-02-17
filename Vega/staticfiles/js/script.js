new WOW().init();

// (function () {

//     var hamburger = {
//         navToggle: document.querySelector('.nav-toggle'),
//         nav: document.querySelector('nav'),

//         doToggle: function (e) {
//             //e.preventDefault();
//             this.navToggle.classList.toggle('expanded');
//             this.nav.classList.toggle('expanded');
//         }
//     };

//     hamburger.navToggle.addEventListener('click', function (e) {
//         hamburger.doToggle(e);
//     });
//     hamburger.nav.addEventListener('click', function (e) {
//         hamburger.doToggle(e);
//     });

// }());

// ----------------------------

var imgBoxs = document.querySelectorAll(".team__imgContainer");

for (var i = 0; i < imgBoxs.length; i++) {
    imgBoxs[i].addEventListener("mouseover", function () {
        this.children[0].children[1].style.height = "100%";
        this.children[0].children[0].style.transform = "scale(1.02)";
    });
    imgBoxs[i].addEventListener("mouseout", function () {
        this.children[0].children[1].style.height = "0";
        this.children[0].children[0].style.transform = "scale(1)";
    });

    imgBoxs[i].addEventListener("click", function () {
        if (this.children[0].children[1].style.height === "100%") {
            this.children[0].children[1].style.height = "0";
        } else {
            this.children[0].children[1].style.height = "100%";
        }
    })

}

