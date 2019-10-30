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

//This callback function is called when the content script has been injected and returned its results

function onPageDetailsReceived(pageDetails){
    document.getElementById('title').value = pageDetails.title;
    document.getElementById('url').value = pageDetails.url;

}

// Global reference to the status display SPAN
var statusDisplay = null;



chrome.storage.local.get(['key'], function(result) {
    console.log(result.key)
    
  })


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