let Backbtn = document.getElementById('back')
let lgobtn = document.getElementById('Logout')
lgobtn.addEventListener('click', clearLocalStorage)
Backbtn.addEventListener('click', previous)




function previous(){
    window.setTimeout(window.close, 500)
    chrome.browserAction.setPopup({popup:"second.html"})
    
}

function clearLocalStorage(){
    chrome.storage.local.clear(function(){
        let error  = chrome.runtime.lastError;
        chrome.browserAction.setPopup({popup:"popup.html"})
        window.setTimeout(window.close, 500)
        if(error){
            console.error(error)
        }
    })
}
