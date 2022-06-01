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