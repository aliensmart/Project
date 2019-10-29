// const axios = require('axios')
let btn = document.getElementById('btn')
btn.addEventListener('click', getToken)

function getToken(){
    
    // if(window.localStorage.getItem('token')== null){
    //     window.location = "popup.html"
let inputPassword = document.getElementById('password').value
let inputUsername = document.getElementById('username').value



    // const sendData = async ()=>{
    //     try{
    //         const data = {
    //             username: inputUsername,
    //             password: inputPassword
    //         }
    //         const res = await axios.post('http://localhost:5000/api/get_api_key', data)
    //         console.log(res.data.api)
    //         alert(res.data.api)
    //         window.localStorage.setItem('token', res.data.api )
    //     }catch(error){
    //         console.log(error)
    //     }
    // }
    // sendData()

    let xhr = new XMLHttpRequest();
    let url = 'http://localhost:5000/api/get_api_key';
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-type', "application/json")
    xhr.onreadystatechange = function(){
        if(xhr.readyState===4 & xhr.status===200){
            let response = JSON.parse(this.responseText)
            chrome.storage.local.set({"key": response.api}, function() {
                console.log('Value is set to ' + response.api);
              })
            console.log(response.api)
            if(response.api){
                chrome.browserAction.setPopup({popup:"second.html"})
            }
        }
    }
    let data = JSON.stringify({username:inputUsername, password:inputPassword});
    xhr.send(data)

}
    
// }else{
//     window.location = "index.html"
// }

