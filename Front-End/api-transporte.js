/**
 * =============================================
 * CARGAR DATOS DE TRANSPORTE DE QUITOSANO
 * =============================================
 * Este script se encarga de obtener los datos de transporte desde la API
 * y actualizar la tabla en la página privada.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Función para cargar los datos de transporte desde la API
    async function fetchTransportData() {
        try {
            const response = await fetch('https://quitosano-production.up.railway.app/api/transporte/');
            
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }
            
            const transportData = await response.json();
            console.log('Datos recibidos:', transportData); // Para depuración
            displayTransportData(transportData);
        } catch (error) {
            console.error('Error al obtener los datos de transporte:', error);
            document.getElementById('transport-data').innerHTML = `
                <tr>
                    <td colspan="7">Error al cargar los datos. Por favor, intente más tarde.</td>
                </tr>
            `;
        }
    }

    // Función para mostrar los datos en la tabla
    function displayTransportData(data) {
        const tableBody = document.getElementById('transport-data');
        
        if (!data || data.length === 0) {
            tableBody.innerHTML = `
                <tr>
                    <td colspan="7">No hay datos de transporte disponibles.</td>
                </tr>
            `;
            return;
        }
        
        // Limpiar la tabla
        tableBody.innerHTML = '';
        
        // Llenar la tabla con los datos de la API
        data.forEach(transport => {
            const row = document.createElement('tr');
            
            // Formatear la fecha para mejor legibilidad
            const fechaTransporte = transport.fecha ? 
                new Date(transport.fecha).toLocaleDateString('es-MX', {
                    day: '2-digit',
                    month: '2-digit',
                    year: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit'
                }) : 'N/A';
            
            row.innerHTML = `
                <td>${transport.id_transporte || 'N/A'}</td>
                <td>${transport.origin || transport.origen || 'N/A'}</td>
                <td>${transport.destino || 'N/A'}</td>
                <td>${transport.producto || 'Quitosano Grado Alimenticio'}</td>
                <td>${transport.cantidad_kg ? transport.cantidad_kg + ' kg' : 'N/A'}</td>
                <td>${fechaTransporte}</td>
                <td>${transport.estado || 'En proceso'}</td>
            `;
            
            tableBody.appendChild(row);
        // Función para crear nuevo transporte
async function createTransport(event) {
    event.preventDefault();
    
    const transportData = {
        origin: document.getElementById('origin').value, // ← Campo corregido
        destino: document.getElementById('destino').value,
        producto: document.getElementById('producto').value,
        cantidad_kg: parseFloat(document.getElementById('cantidad_kg').value),
        // fecha: new Date().toISOString() // Si el servidor no la genera
    };

    try {
        const response = await fetch('https://quitosano-production.up.railway.app/api/transporte/crear/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(transportData)
        });

            if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
            
            alert('Transporte creado exitosamente!');
            fetchTransportData();
            event.target.reset();
        } catch (error) {
            console.error('Error al crear transporte:', error);
            alert('Error al crear transporte');
        }
    }

    // Función para actualizar transporte
    async function updateTransport(event) {
        event.preventDefault();
        
        const transportData = {
            id_transporte: document.getElementById('edit-id').value,
            origen: document.getElementById('edit-origen').value,
            destino: document.getElementById('edit-destino').value,
            cantidad_kg: document.getElementById('edit-cantidad').value,
            estado: document.getElementById('edit-estado').value
        };

        try {
            const response = await fetch(`https://quitosano-production.up.railway.app/api/transporte/${transportData.id_transporte}/actualizar/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(transportData)
            });

            if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
            
            alert('Transporte actualizado exitosamente!');
            fetchTransportData();
            cancelEdit();
        } catch (error) {
            console.error('Error al actualizar transporte:', error);
            alert('Error al actualizar transporte');
        }
    }

    // Función para cargar datos en formulario de edición
    function loadEditForm(transport) {
        document.getElementById('edit-transport-form').style.display = 'block';
        document.getElementById('edit-id').value = transport.id_transporte;
        document.getElementById('edit-origen').value = transport.origin || transport.origen;
        document.getElementById('edit-destino').value = transport.destino;
        document.getElementById('edit-cantidad').value = transport.cantidad_kg;
        document.getElementById('edit-estado').value = transport.estado;
    }

    // Función para cancelar edición
    function cancelEdit() {
        document.getElementById('edit-transport-form').style.display = 'none';
        document.getElementById('edit-transport-form').reset();
    }

    // Event Listeners para los formularios
    document.getElementById('create-transport-form').addEventListener('submit', createTransport);
    document.getElementById('edit-transport-form').addEventListener('submit', updateTransport);

    // Modificar la función displayTransportData para agregar botones de edición
    function displayTransportData(data) {
        // ... código existente ...
        
        data.forEach(transport => {
            const row = document.createElement('tr');
            
            // ... código existente para las celdas ...
            
            // Agregar celda de acciones
            const actionCell = document.createElement('td');
            actionCell.innerHTML = `
                <button class="edit-btn" onclick="loadEditForm(${JSON.stringify(transport)})">
                    <i class="fas fa-edit"></i> Editar
                </button>
            `;
            row.appendChild(actionCell);
            
            tableBody.appendChild(row);
        });
    }
        });
    }

    // Cargar los datos cuando la página esté lista
    fetchTransportData();

    // Opcional: Actualizar datos cada 60 segundos
    setInterval(fetchTransportData, 60000);
});
