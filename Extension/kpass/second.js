
let lgobtn = document.getElementById('Logout')
let save = document.getElementById('save')
let view = document.getElementById('passwords')

lgobtn.addEventListener('click', clearLocalStorage)
view.addEventListener('click', viewPass)
save.addEventListener('click', saveData)

function clearLocalStorage(){
    chrome.storage.local.clear(function(){
        let error  = chrome.runtime.lastError;
        chrome.browserAction.setPopup({popup:"popup.html"})
        if(error){
            console.error(error)
        }
    })
}

function viewPass(){
    window.setTimeout(window.close, 500)
    chrome.browserAction.setPopup({popup:"viewPassword.html"})
}


//This callback function is called when the content script has been injected and returned its results

function onPageDetailsReceived(pageDetails){
    document.getElementById('title').value = pageDetails.title;
    document.getElementById('url').value = pageDetails.url;
    let url = pageDetails.url;
    console.log(url)
    
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