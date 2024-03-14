
document.addEventListener('DOMContentLoaded', function() {
    // Obtén los valores desde los atributos de datos
    var gamaBaja = parseInt(document.getElementById('myPieChart').getAttribute('data-gama-baja'));
    var gamaMedia = parseInt(document.getElementById('myPieChart').getAttribute('data-gama-media'));
    var gamaAlta = parseInt(document.getElementById('myPieChart').getAttribute('data-gama-alta'));

    // Crea el gráfico con los valores obtenidos
    crearGrafico(gamaBaja, gamaMedia, gamaAlta);
});

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



