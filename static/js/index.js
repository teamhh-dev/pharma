function toggleNavItemText() {
    let navItemTextElements = document.getElementsByClassName("nav-item-text");
    let toggleBar = document.getElementById("toggle-menu");

    if (toggleBar.classList.contains("fa-align-left")) {
        toggleBar.classList.replace("fa-align-left", "fa-align-justify");
        for (let item of navItemTextElements) {


            item.classList.toggle("show");

        }

    } else {
        toggleBar.classList.replace("fa-align-justify", "fa-align-left");
        for (let item of navItemTextElements) {


            item.classList.toggle("show");


        }

    }



}

function animate() {
    let navbar = document.getElementById("navbar");
    navbar.addEventListener("mouseover", function() {
        let child = navbar.children;
        let navItemText = document.getElementsByClassName("nav-item-text");

        for (item of navItemText) {
            item.classList.add("show");
        }
    });
    navbar.addEventListener("mouseout", function() {
        let child = navbar.children;
        let navItemText = document.getElementsByClassName("nav-item-text");

        for (item of navItemText) {
            item.classList.remove("show");
        }
    });
}

animate();