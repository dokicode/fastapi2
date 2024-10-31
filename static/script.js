function sendAjax(){
    console.log('sendAjax');
    fetch('/endpoint_ajax', {
        method: 'POST',
        headers: {
            'Content-Type': 'application-json;charset=utf-8'
        },
        body: JSON.stringify({
            data: 'some useful data'
        })
    }).then( response => {
        return response.json()
    }).then(data => {
        console.log(data)
    })
}