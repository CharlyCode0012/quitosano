document.addEventListener('DOMContentLoaded', function() {
    const AMBIENTE_API_URL = 'https://quitosano-production.up.railway.app/api/ambiente';
    const tableBody = document.getElementById('temp-hum-data');
    const createForm = document.getElementById('create-ambiente-form');
    const editForm = document.getElementById('edit-ambiente-form');

    // ==================== GET ====================
    async function loadAmbienteData() {
        try {
            const response = await fetch(AMBIENTE_API_URL);
            if (!response.ok) throw new Error(`Error ${response.status}`);
            const data = await response.json();
            updateTable(data);
        } catch (error) {
            console.error('Error:', error);
            showError();
        }
    }

    // ==================== POST ====================
    async function createAmbiente(event) {
        event.preventDefault();
        
        const formData = {
            id_transporte: createForm.querySelector('#create-id-transporte').value,
            temperatura_actual: parseFloat(createForm.querySelector('#create-temp-actual').value),
            temperatura_min: parseFloat(createForm.querySelector('#create-temp-min').value),
            temperatura_max: parseFloat(createForm.querySelector('#create-temp-max').value),
            humedad_actual: parseFloat(createForm.querySelector('#create-hum-actual').value),
            humedad_min: parseFloat(createForm.querySelector('#create-hum-min').value),
            humedad_max: parseFloat(createForm.querySelector('#create-hum-max').value)
        };

        try {
            const response = await fetch(`${AMBIENTE_API_URL}/crear/`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(formData)
            });

            if (!response.ok) throw new Error(await response.text());
            
            alert('Registro creado exitosamente!');
            createForm.reset();
            await loadAmbienteData();
        } catch (error) {
            console.error('Error al crear:', error);
            alert(`Error: ${error.message}`);
        }
    }

    // ==================== PUT ====================
    let currentEditId = null;

    function openEditForm(item) {
        currentEditId = item.id_transporte;
        editForm.querySelector('#edit-temp-actual').value = item.temperatura_actual;
        editForm.querySelector('#edit-temp-min').value = item.temperatura_min;
        editForm.querySelector('#edit-temp-max').value = item.temperatura_max;
        editForm.querySelector('#edit-hum-actual').value = item.humedad_actual;
        editForm.querySelector('#edit-hum-min').value = item.humedad_min;
        editForm.querySelector('#edit-hum-max').value = item.humedad_max;
        editForm.style.display = 'block';
    }

    async function updateAmbiente(event) {
        event.preventDefault();

        const formData = {
            temperatura_actual: parseFloat(editForm.querySelector('#edit-temp-actual').value),
            temperatura_min: parseFloat(editForm.querySelector('#edit-temp-min').value),
            temperatura_max: parseFloat(editForm.querySelector('#edit-temp-max').value),
            humedad_actual: parseFloat(editForm.querySelector('#edit-hum-actual').value),
            humedad_min: parseFloat(editForm.querySelector('#edit-hum-min').value),
            humedad_max: parseFloat(editForm.querySelector('#edit-hum-max').value)
        };

        try {
            const response = await fetch(`${AMBIENTE_API_URL}/${currentEditId}/actualizar/`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(formData)
            });

            if (!response.ok) throw new Error(await response.text());
            
            alert('Registro actualizado!');
            editForm.reset();
            editForm.style.display = 'none';
            await loadAmbienteData();
        } catch (error) {
            console.error('Error al actualizar:', error);
            alert(`Error: ${error.message}`);
        }
    }

    // ==================== Helpers ====================
    function updateTable(data) {
        tableBody.innerHTML = '';
        
        data.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.id_transporte}</td>
                <td>${item.producto || 'Quitosano'}</td>
                <td class="${getStatusClass(item.temperatura_actual, item.temperatura_min, item.temperatura_max)}">
                    ${item.temperatura_actual}°C
                </td>
                <td>${item.temperatura_min}°C</td>
                <td>${item.temperatura_max}°C</td>
                <td class="${getStatusClass(item.humedad_actual, item.humedad_min, item.humedad_max)}">
                    ${item.humedad_actual}%
                </td>
                <td>${item.humedad_min}%</td>
                <td>${item.humedad_max}%</td>
                <td>
                    <button class="edit-btn" onclick="openEditForm(${JSON.stringify(item)})">
                        <i class="fas fa-edit"></i>
                    </button>
                </td>
            `;
            tableBody.appendChild(row);
        });
    }

    function getStatusClass(current, min, max) {
        return (current < min || current > max) ? 'warning' : '';
    }

    // Event Listeners
    createForm.addEventListener('submit', createAmbiente);
    editForm.querySelector('#cancel-edit').addEventListener('click', () => {
        editForm.style.display = 'none';
    });
    editForm.addEventListener('submit', updateAmbiente);

    // Inicialización
    loadAmbienteData();
    setInterval(loadAmbienteData, 60000);
});