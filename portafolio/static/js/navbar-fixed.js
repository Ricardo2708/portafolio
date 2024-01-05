document.addEventListener("DOMContentLoaded", (e) => {
    let navbar = document.querySelector('.menu__content')
    let body = document.querySelector('body')
    
    window.addEventListener("scroll", () =>{
        let scroll = window.scrollY

        if(scroll > 120 ){
            navbar.classList.add("menu__navbar--fixed");
            let opacityNavbar = document.querySelector(".menu__navbar--fixed")
            body.classList.add("body-scroll")
            opacityNavbar.style.opacity = 1
        }else{
            navbar.classList.remove("menu__navbar--fixed");
            body.classList.remove("body-scroll")
        }
    })

})