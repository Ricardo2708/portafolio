document.addEventListener("DOMContentLoaded", (e) =>{
    let switcher = document.querySelector(".switcher__btn")

    let light = document.querySelector(".switcher__icon-light")
    let dark = document.querySelector(".switcher__icon-dark")

    let logo = document.querySelector(".navbar__logo-light")
    let logoMovil = document.querySelector(".menu-mobile__logo")


    let currentTheme = localStorage.getItem("theme")|| "light";
    if (currentTheme === "dark") {
        loadDark();
    } else {
        loadLight();
    }

    switcher.addEventListener("click", () =>{
        if(currentTheme === "dark"){
            loadLight()
        }else{
            loadDark()
        }
    })

    function loadLight(){
        let theme_dark = document.querySelector("#theme-dark")
        let head =document.head;
        if (theme_dark) {
            head.removeChild(theme_dark);
        }
        light.style.display = "block"
        dark.style.display = "none"
        logo.src = icon1;
        logoMovil.src = icon1;
        localStorage.setItem("theme", "light");
        currentTheme = "light"; // Actualizar currentTheme
    }

    function loadDark(){
        let head =document.head;
        let link = document.createElement("link");
        link.rel = "stylesheet";
        link.type = "text/css";
        link.href = cssUrl;
        link.id = "theme-dark"

        head.appendChild(link);
        dark.style.display = "block"
        light.style.display = "none"
        logo.src = icon2;
        logoMovil.src = icon2;
        localStorage.setItem("theme", "dark");
        currentTheme = "dark"; // Actualizar currentTheme

    }

    
})