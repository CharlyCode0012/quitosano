/**
 * =============================================
 * VALIDACIÓN DEL FORMULARIO DE LOGIN CON API
 * =============================================
 * A este script se le requiere un modal ya existente en el HTML con los IDs adecuados.
 */
document.querySelector('.login-form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Previene el envío tradicional del formulario

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        // Realiza la solicitud a la API para verificar las credenciales
        const response = await fetch(`https://quitosano-production.up.railway.app/api/usuario/?username=${username}&password=${password}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();

        // Verifica si la respuesta es exitosa y el usuario existe
        if (response.ok && data.length > 0) {
            // Si el usuario existe, redirige a la página privada
            window.location.href = "privado.html";
        } else {
            // Muestra alerta si las credenciales son incorrectas
            alert('Credenciales incorrectas. Intente nuevamente.');
        }
    } catch (error) {
        console.error('Error en la conexión a la API:', error);
        alert('Hubo un error al intentar iniciar sesión. Intente nuevamente más tarde.'); // Notifica al usuario de un error en la conexión
    } finally {
        // Cierra el modal independientemente del resultado
        const loginModal = document.getElementById('loginModal');
        loginModal.classList.remove('active'); // Oculta el modal
        document.body.style.overflow = 'auto'; // Restaura el scroll
    }
});