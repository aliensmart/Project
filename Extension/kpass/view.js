let Backbtn = document.getElementById('back')
let lgobtn = document.getElementById('Logout')
let toggle = document.getElementById("passview")
lgobtn.addEventListener('click', clearLocalStorage)
Backbtn.addEventListener('click', previous)

toggle.addEventListener('click', toggleView)

function toggleView(){
    let field = document.getElementById('password');
    if(field.type=== "password"){
        field.type = "text"
    }else{
        field.type = "password"
    }
}

window.addEventListener('load', (event) => {
    chrome.storage.local.get(['key'], function(result){
        let token = result.key
        function onPageDetailsReceived(pageDetails){
            document.getElementById('title').value = pageDetails.title;
            document.getElementById('url').value = pageDetails.url;

            let query = pageDetails.title;
            console.log(query)
            let xhr = new XMLHttpRequest();
            let url = `http://localhost:5000/api/${token}/${query}`;
            xhr.open('GET', url, true);
            xhr.setRequestHeader('Content-type', "application/json");
            xhr.send()
            console.log(xhr)
            xhr.onreadystatechange = function(){
                
                if(xhr.readyState===4 & xhr.status===200){
                    let res = JSON.parse(xhr.response)
                    res = res.your_pass
                    console.log(res)
                    document.getElementById('email').value = res.email;
                    document.getElementById('password').value = res.password_hash;
                    document.getElementById('username').value = res.username
                }
            }

            
        }

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
        
    })
  })

function previous(){
    window.setTimeout(window.close, 500)
    chrome.browserAction.setPopup({popup:"second.html"})
    window.setTimeout(window.location.replace("second.html"), 500)
    
}

function clearLocalStorage(){
    chrome.storage.local.clear(function(){
        let error  = chrome.runtime.lastError;
        chrome.browserAction.setPopup({popup:"popup.html"})
        window.setTimeout(window.location.replace("popup.html"), 500)
        window.setTimeout(window.close, 500)
        if(error){
            console.error(error)
        }
    })
}
