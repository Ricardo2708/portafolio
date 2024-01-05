document.addEventListener("DOMContentLoaded", (e) =>{
    let button_form = document.querySelector(".contact__btn-formulario")
    if (button_form) {
      button_form.addEventListener("click", (e) =>{
          e.preventDefault()
          Toastify({
              text: "Formulario No Disponible",
              duration: 3000
          }).showToast();
      })
    }

    let button_portafolio = document.querySelectorAll(".boton_portafolio")
    button_portafolio.forEach(element => {
      element.addEventListener("click", (e) =>{
        e.preventDefault()
        Toastify({
            text: "Te Encuentras En Portafolio",
            duration: 3000,
            style: {
              background: "linear-gradient(to right, #FF8800, #FF0000)",
            }
        }).showToast();
    })
    });


    const swiper = new Swiper('.swiper', {
        // Optional parameters
        direction: 'horizontal',
        loop: true,

        slidesPerView: 4,
        // Opción para habilitar el cambio automático entre los elementos del carrusel
        autoplay: {
          delay: 2500,
          disableOnInteraction: false,
        },
        // Opción para permitir el desplazamiento manual mediante gestos en dispositivos táctiles
        touchMoveStopPropagation: true,

        breakpoints: {
          220: {
            slidesPerView: 1,
            spaceBetween: 20,
          },
          460: {
            slidesPerView: 2,
            spaceBetween: 20,
          },
          640: {
            slidesPerView: 3,
            spaceBetween: 20,
          },
          768: {
            slidesPerView: 4,
            spaceBetween: 20,
          },
          1024: {
            slidesPerView: 4,
            spaceBetween: 5,
          },
        },
    });

    const swiper2 = new Swiper('.swiper2', {
      // Optional parameters
      direction: 'horizontal',
      loop: true,
      slidesPerView: 1,
      // Opción para habilitar el cambio automático entre los elementos del carrusel
      autoplay: {
        delay: 5500,
        disableOnInteraction: false,
      },
      // Opción para permitir el desplazamiento manual mediante gestos en dispositivos táctiles
      touchMoveStopPropagation: true,
      breakpoints: {
        220: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        460: {
          slidesPerView: 2,
          spaceBetween: 20,
        },

        768: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        992: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
        1220: {
          slidesPerView: 4,
          spaceBetween: 20,
        },
      },

      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },

      pagination: {
        el: '.swiper-pagination',
      },
    });

    const swiper3 = new Swiper('.swiper3', {
      // Optional parameters
      direction: 'horizontal',
      loop: true,
      slidesPerView: 1,
      // Opción para habilitar el cambio automático entre los elementos del carrusel
      autoplay: {
        delay: 5500,
        disableOnInteraction: false,
      },
      // Opción para permitir el desplazamiento manual mediante gestos en dispositivos táctiles
      touchMoveStopPropagation: true,
      breakpoints: {
        220: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        460: {
          slidesPerView: 2,
          spaceBetween: 20,
        },

        768: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        992: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
        1220: {
          slidesPerView: 4,
          spaceBetween: 30,
        },
      },

      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },

      pagination: {
        el: '.swiper-pagination3',
      },
    });

    let link__github = document.querySelectorAll('.link__github')
    link__github.forEach(element => {
      if (element.href.includes("none")) {
        element.addEventListener("click", (e) =>{
          e.preventDefault()
          Toastify({
              text: "No Se Encontro El Repositorio",
              duration: 3000,
              style: {
                background: "linear-gradient(to right, #FF8800, #FF0000)",
              }
          }).showToast();
      })
      }
    })
})