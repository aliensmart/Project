// const axios = require('axios');

function getToken(){
    if(window.localStorage.getItem('token')== null){
        window.location = "popup.html"
let inputPassword = document.getElementById('password').value
let inputUsername = document.getElementById('username').value
// let btn = document.getElementById('btn')


    const sendData = async ()=>{
        try{
            const data = {
                username: inputUsername,
                password: inputPassword
            }
            const res = await axios.post('http://localhost:5000/api/get_api_key', data)
            console.log(res.data.api)
            window.localStorage.setItem('token', res.data.api )
        }catch(error){
            console.log(error)
        }
    }
    sendData()

    
}else{
    window.location = "index.html"
}
}

