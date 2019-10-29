let lgobtn = document.getElementById('Logout')
lgobtn.addEventListener('click', clearLocalStorage)

function clearLocalStorage(){
    chrome.storage.local.clear(function(){
        let error  = chrome.runtime.lastError;
        chrome.browserAction.setPopup({popup:"popup.html"})
        if(error){
            console.error(error)
        }
    })
}




chrome.storage.local.get(['key'], function(result) {
    console.log(result.key)
    
  })
