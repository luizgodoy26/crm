function render_total_clients(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_clients').innerHTML = data.total
    })
}

function render_total_contracts(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_contracts').innerHTML = data.total
    })
}

function render_total_received(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_received').innerHTML = data.total
    })
}


function render_total_pending(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_pending').innerHTML = data.total
    })
}


function render_month_received(url){
        fetch(url, {
            method: 'get',
        }).then(function(result){
            return result.json()
        }).then(function(data){

            const ctx = document.getElementById('month_income');
            const myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Income',
                        data: data.data,
                        borderWidth: 1,
                        backgroundColor: [
                          'rgba(242, 82, 82)',
                          'rgba(34, 242, 155)',
                          'rgba(100, 61, 242)',
                          'rgba(217, 85, 181)',
                        ],
                        borderRadius: 10,
                    }]
                },
                options: {
                    plugins: {
                        legend: {
                            display: false,
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                display: false
                            }
                         },
                        y: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                display: false
                            }
                        }
                    }
                }

            });

        })
}