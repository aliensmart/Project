// Send a message containing the page details back to the event page
chrome.runtime.sendMessage({
    'title': window.location.hostname,
    'url': window.location.protocol + "//"+ window.location.hostname,
});

forms = document.getElementsByName('form')
for (let form of forms){
    console.log(typeof(form))
}

// //start connection in content script
// let contentPort = chrome.runtime.connect({
//     name: 'background-content'
//  });
 
//  //Listen for runtime message
//  chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
//     //Retrieve offset dimension
//     console.log(message)
//     if(message.action === 'GET_DIMENSION') {
//        contentPort.postMessage({
//           type: 'DIMENSION', 
//           payload: {
//              height: document.body.offsetHeight,
//              width: document.body.offsetWidth       
//           }
//        });
//     }
//  });