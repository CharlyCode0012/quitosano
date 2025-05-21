/**
 * =============================================
 * FUNCIONALIDAD DEL MODAL DE LOGIN
 * =============================================
 */

// Obtiene referencias a los elementos del DOM
const loginBtn = document.getElementById('loginBtn'); // Botón para abrir modal
const loginModal = document.getElementById('loginModal'); // Modal en sí
const closeBtn = document.getElementById('closeBtn'); // Botón para cerrar modal

/**
 * Evento para abrir el modal de login
 */
loginBtn.addEventListener('click', () => {
    loginModal.classList.add('active'); // Muestra el modal
    document.body.style.overflow = 'hidden'; // Deshabilita el scroll de la página
});

/**
 * Evento para cerrar el modal al hacer clic en el botón de cerrar
 */
closeBtn.addEventListener('click', () => {
    loginModal.classList.remove('active'); // Oculta el modal
    document.body.style.overflow = 'auto'; // Restaura el scroll de la página
});

/**
 * Evento para cerrar el modal al hacer clic fuera del contenido
 */
loginModal.addEventListener('click', (e) => {
    // Si el clic fue directamente en el fondo del modal (no en el contenido)
    if (e.target === loginModal) {
        loginModal.classList.remove('active'); // Oculta el modal
        document.body.style.overflow = 'auto'; // Restaura el scroll
    }
});