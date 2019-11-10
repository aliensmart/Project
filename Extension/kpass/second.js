//-----------------------------------------------------------------------------------------------------------
//--Global Variables-----------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------------------------
let lgobtn = document.getElementById('Logout')
let save = document.getElementById('save')
let view = document.getElementById('passwords')
let toggle = document.getElementById("passview")
let generate = document.getElementById("generate")

//---------------------------------------------------------------------------------------------------------
//--Buttons events-----------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------------------------
lgobtn.addEventListener('click', clearLocalStorage)
view.addEventListener('click', viewPass)
save.addEventListener('click', saveData)
toggle.addEventListener('click', toggleView)
generate.addEventListener('click', generatePass)

//---------------------------------------------------------------------------------------------------------
//--Toggle to the view page-----------------------------------------------------------------------------------------
//---------------------------------------------------------------------------------------------------------
function toggleView(){
    let field = document.getElementById('password');
    if(field.type=== "password"){
        field.type = "text"
    }else{
        field.type = "password"
    }
}

//---------------------------------------------------------------------------------------------------------
//--Generate Password function-----------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------------------------
function generatePass(){
    let length = parseInt(document.getElementById("lenght").value)
    let uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let lowercase = 'abcdefghijklmnopqrstuvwxyz';
    let numbers = '0123456789';
    let symbols = '!"#$%&\'()*+,-./:;<=>?@^[\\]^_`{|}~';
    let all = uppercase + lowercase + numbers + symbols;

    let password = '';
    
    for (let i=0; i<=length; i++){
        let char = Math.floor(Math.random() * all.length)
        password += all.substring(char, char + 1)
    }
    let newPass = password;
    document.getElementById('password').value = newPass
}

function clearLocalStorage(){
    chrome.storage.local.clear(function(){
        let error  = chrome.runtime.lastError;
        chrome.browserAction.setPopup({popup:"popup.html"})
        window.setTimeout(window.location.replace("popup.html"), 500)
        if(error){
            console.error(error)
        }
    })
}

function viewPass(){
    window.setTimeout(window.close, 500)
    chrome.browserAction.setPopup({popup:"viewPassword.html"})
    window.setTimeout(window.location.replace("viewPassword.html"), 500)
}


//This callback function is called when the content script has been injected and returned its results

function onPageDetailsReceived(pageDetails){
    document.getElementById('title').value = pageDetails.title;
    document.getElementById('url').value = pageDetails.url;
    
}


// Global reference to the status display SPAN
let statusDisplay = null;
function saveData(){
    event.preventDefault();
    chrome.storage.local.get(['key'], function(result) {
        let token = result.key
        let url = `http://localhost:5000/api/${token}/passwords_post`

        let inputEmail = document.getElementById('email').value;
        let inputUser = document.getElementById('username').value;
        let inputPassword = document.getElementById('password').value;
        let inputUrl = document.getElementById('url').value;
        let inputSite = document.getElementById('title').value;

        let xhr = new XMLHttpRequest()
        xhr.open('POST', url, true)
        xhr.setRequestHeader('Content-type', "application/json")
        xhr.onreadystatechange = function(){
            console.log(xhr)
            if(xhr.readyState===4 & xhr.status===200){
                statusDisplay.innerHTML = 'Saved!';
                window.setTimeout(window.close, 1000);
            } else {
                // Show what went wrong
                statusDisplay.innerHTML = 'Error saving: ' + xhr.statusText;
            }
        }
        let data = JSON.stringify({
            
            username: inputUser,
            password: inputPassword,
            url: inputUrl,
            email: inputEmail,
            site_name:inputSite
        })
        console.log(data)
        xhr.send(data)

      })
    
}
      // When the popup HTML has loaded
window.addEventListener('load', function(evt) {
    // Cache a reference to the status display SPAN
    statusDisplay = document.getElementById('status-display');
    // Handle the bookmark form submit event with our addBookmark function
    // document.getElementById('addbookmark')
    //         .addEventListener('submit', addBookmark);
    // Get the event page
    chrome.runtime.getBackgroundPage(function(eventPage) {
        // Call the getPageInfo function in the event page, passing in
        // our onPageDetailsReceived function as the callback. This
        // injects content.js into the current tab's HTML
        eventPage.getPageDetails(onPageDetailsReceived)
    });
});