
document.addEventListener('DOMContentLoaded', function() {
    // Obtén los valores desde los atributos de datos
    var gamaBaja = parseInt(document.getElementById('myPieChart').getAttribute('data-gama-baja'));
    var gamaMedia = parseInt(document.getElementById('myPieChart').getAttribute('data-gama-media'));
    var gamaAlta = parseInt(document.getElementById('myPieChart').getAttribute('data-gama-alta'));

    // Crea el gráfico con los valores obtenidos
    crearGrafico(gamaBaja, gamaMedia, gamaAlta);
});


// funcion para crearGrafico 
function crearGrafico(gamaBaja, gamaMedia, gamaAlta) {
    var ctx = document.getElementById('myPieChart').getContext('2d');
    var data = {
        labels: ['Gama Baja', 'Gama Media', 'Gama Alta'],
        datasets: [{
            data: [gamaBaja, gamaMedia, gamaAlta],
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
        }]
    };
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'bottom',
            },
        },
    });
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('/estadisticas/estadisticas-ocupadas-json/')
        .then(response => response.json())
        .then(data => {
            // Ahora data contiene gamaBajaOcupada, gamaMediaOcupada, gamaAltaOcupada
            console.log(data); // Puedes quitar este log después de verificar que funciona
            // Suponiendo que tienes una función para crear el gráfico que acepta estos valores
            crearGraficoOcupadas(document.getElementById('myPieChartOcupadas'), data.gamaBajaOcupada, data.gamaMediaOcupada, data.gamaAltaOcupada);
        })
        .catch(error => console.error('Error al obtener los datos:', error));
});

// Asegúrate de que la función crearGraficoOcupadas esté definida para usar los datos obtenidos
function crearGraficoOcupadas(elemento, gamaBajaOcupada, gamaMediaOcupada, gamaAltaOcupada) {
    var ctx = elemento.getContext('2d');
    var data = {
        labels: ['Gama Baja', 'Gama Media', 'Gama Alta'],
        datasets: [{
            data: [gamaBajaOcupada, gamaMediaOcupada, gamaAltaOcupada],
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
        }]
    };
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'bottom',
            },
        },
    });
}
