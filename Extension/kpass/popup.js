let btn = document.getElementById('btn')
btn.addEventListener('click', getToken)

function getToken(){

let inputPassword = document.getElementById('password').value
let inputUsername = document.getElementById('username').value

    let xhr = new XMLHttpRequest();
    let url = 'http://localhost:5000/api/get_api_key';
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-type', "application/json")
    xhr.onreadystatechange = function(){
        if(xhr.readyState===4 & xhr.status===200){
            let response = JSON.parse(this.responseText)
            console.log(response)
            chrome.storage.local.set({"key": response.api}, function() {
                console.log('Value is set to ' + response.api);
              })
            console.log(response.api)
            if(response.api){
                
                chrome.browserAction.setPopup({popup:"second.html"})
                window.setTimeout(window.close, 500)
            }
        }
    }
    let data = JSON.stringify({username:inputUsername, password:inputPassword});
    xhr.send(data)

}
