/**
 * =============================================
 * MANEJO DEL FORMULARIO DE REPORTES
 * =============================================
 * 
 * Procesa el envío del formulario de reportes
 * (Nota: Actualmente solo muestra los datos en consola)
 */
document.querySelector('.report-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Previene el envío tradicional
    
    // Recopila los datos del formulario en un objeto
    const reportData = {
        nombre: document.getElementById('nombre').value,
        puesto: document.getElementById('puesto').value,
        condiciones: document.getElementById('condiciones').value,
        transporteId: document.getElementById('transporte-id').value,
        temperatura: document.getElementById('temperatura').value,
        cantidad: document.getElementById('cantidad').value,
        destino: document.getElementById('destino').value,
        observaciones: document.getElementById('observaciones').value
    };
    
    // Muestra los datos en consola (simulando envío)
    console.log('Reporte generado:', reportData);
    
    // Notifica al usuario
    alert('Reporte generado con éxito');
    
    // Resetea el formulario
    this.reset();
});
