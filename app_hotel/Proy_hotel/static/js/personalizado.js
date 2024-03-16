
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
            title: {
                display: true,
                text: 'Habitaciones'
            }
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
        labels: ['Gama Baja Ocuapada', 'Gama Media Ocuapada', 'Gama Alta Ocuapada'],
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
            title: {
                display: true,
                text: 'Habitaciones ocupadas'
            }
        },
    });
}


document.addEventListener('DOMContentLoaded', function() {
    fetch('/estadisticas/obtener_estadisticas_reservas_ajax/')
        .then(response => response.json())
        .then(data => {
            // Ahora data contiene reservas_pagadas, reservas_no_pagadas y clientes_con_reserva
            console.log(data); // Puedes quitar este log después de verificar que funciona
            // Suponiendo que tienes una función para crear el gráfico que acepta estos valores
            crearGraficoReservasPagadas(document.getElementById('myPieChartReservasPagadas'), data.reservas_pagadas, data.reservas_no_pagadas);
            crearGraficoClientesConReserva(document.getElementById('myPieChartClientesConReserva'), data.clientes_con_reserva);
        })
        .catch(error => console.error('Error al obtener los datos:', error));
});

function crearGraficoReservasPagadas(elemento, reservasPagadas, reservasNoPagadas) {
    var ctx = elemento.getContext('2d');
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Reservas Pagadas', 'Reservas No Pagadas'],
            datasets: [{
                data: [reservasPagadas, reservasNoPagadas],
                backgroundColor: ['#FF6384', '#36A2EB'],
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'bottom',
            },
            title: {
                display: true,
                text: 'Reservas'
            }
        },
    });
}


function crearGraficoClientesConReserva(elemento, clientesConReserva) {
    var ctx = elemento.getContext('2d');
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Clientes con Reserva', 'Clientes sin Reserva'],
            datasets: [{
                data: [clientesConReserva],
                backgroundColor: ['#FF6384', '#36A2EB'],
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position: 'bottom',
            },
            title: {
                display: true,
                text: 'Clientes'
            }
        },
    });
}

/*
$.ajax({
    url: '/estadisticas/estadisticas-ocupadas-json/',
    type: 'get',
    dataType: 'json',
    success: function(data) {
        var ctx = document.getElementById('myPieChartreservas').getContext('2d');
        var myPieChartreservas = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Gama Baja', 'Gama Media', 'Gama Alta'],
                datasets: [{
                    data: [data.gama_baja, data.gama_media, data.gama_alta],
                    backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                }]
            }
        });
    }
});

$(document).ready(function(){
    $.ajax({
        url: '/estadisticas/estadisticas-ocupadas-json/',
        type: 'get',
        dataType: 'json',
        success: function(data) {
            var ctx = document.getElementById('myPieChartreservas').getContext('2d');
            var myPieChartreservas = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: ['Gama Baja Ocupada', 'Gama Media Ocupada', 'Gama Alta Ocupada'],
                    datasets: [{
                        data: [data.gamaBajaOcupada, data.gamaMediaOcupada, data.gamaAltaOcupada],
                        backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: {
                        position: 'bottom',
                    },
                    title: {
                        display: true,
                        text: 'Habitaciones Ocupadas por Gama'
                    }
                }
            });
        }
    });
});*/