document.addEventListener('DOMContentLoaded', function () {
    const botonEliminar = document.querySelectorAll('.botonEliminar');

    botonEliminar.forEach(boton => {
        boton.addEventListener('click', (event) => {
            event.preventDefault();
            const url = event.currentTarget.getAttribute('href');
            const tipo = event.currentTarget.getAttribute('data-tipo');
            const confirmacion = confirm(`¿Estás seguro que quieres eliminar este ${tipo}?`);

            if (confirmacion) {
                window.location.href = url;
            }
        });
    });
});