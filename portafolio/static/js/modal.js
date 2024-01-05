// Obtén el modal y el botón para mostrarlo
var modal = document.getElementById('miModal');
var btnMostrarModal = document.getElementById('mostrarModal');
var modalContenido = document.querySelector('.modal-contenido');

function mostrarModal() {
    modal.style.display = 'block';
    setTimeout(function() {
      modal.classList.add('mostrar');
      modalContenido.style.opacity = "1"
    }, 300); 
  }


function cerrarModal() {
    modalContenido.style.opacity = "0"
    setTimeout(function() {
        modal.classList.remove('mostrar');
        modal.style.display = 'none';
    }, 300);
}



window.onclick = function(event) {
  if (event.target == modal) {
    modalContenido.style.opacity = "0"
    setTimeout(function() {
        modal.classList.remove('mostrar');
        modal.style.display = 'none';
    }, 300);
  }
}

btnMostrarModal.onclick = mostrarModal;