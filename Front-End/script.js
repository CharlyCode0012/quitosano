/**
 * =============================================
 * OBSERVADOR DE INTERSECCIÓN PARA ANIMACIONES AL HACER SCROLL
 * =============================================
 * 
 * Este observer detecta cuando los elementos entran en el viewport
 * y les añade la clase 'visible' para activar las animaciones CSS
 */
const observer = new IntersectionObserver((entries) => {
    // Itera sobre cada entrada observada
    entries.forEach(entry => {
        // Si el elemento está intersectando (visible en el viewport)
        if (entry.isIntersecting) {
            // Añade la clase 'visible' para activar la animación
            entry.target.classList.add('visible');
        }
    });
}, { 
    threshold: 0.1 // Dispara la animación cuando el 10% del elemento es visible
});

// Observa todos los elementos con las clases 'service-card' y 'process-step'
document.querySelectorAll('.service-card, .process-step').forEach((el) => {
    observer.observe(el);
});

/**
 * =============================================
 * SCROLL SUAVE PARA ENLACES DE NAVEGACIÓN INTERNA
 * =============================================
 * 
 * Implementa un scroll suave cuando se hace clic en enlaces internos (#)
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault(); // Previene el comportamiento por defecto
        
        // Obtiene el elemento destino del enlace y hace scroll suave hacia él
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth' // Efecto de desplazamiento suave
        });
    });
});

/**
 * =============================================
 * OBSERVADOR ADICIONAL PARA MÁS ELEMENTOS ANIMADOS
 * =============================================
 * 
 * Extiende el observer inicial para incluir los bloques de visión/misión
 */
document.querySelectorAll('.service-card, .process-step, .vm-block').forEach((el) => {
    observer.observe(el);
});

/**
 * =============================================
 * OBSERVADOR DE INTERSECCIÓN MEJORADO (ALTERNATIVA)
 * =============================================
 * 
 * Versión alternativa del observer que se ejecuta cuando el DOM está cargado
 */
document.addEventListener('DOMContentLoaded', () => {
    // Selecciona todos los elementos que deben animarse
    const elementsToAnimate = document.querySelectorAll('.service-card, .vm-block, .process-step');

    // Crea un nuevo observador de intersección
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible'); // Activa la animación
            }
        });
    }, {
        threshold: 0.2 // Dispara cuando el 20% del elemento es visible
    });

    // Observa cada elemento seleccionado
    elementsToAnimate.forEach(element => observer.observe(element));
});


