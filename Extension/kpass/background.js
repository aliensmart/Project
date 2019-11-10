// This function is called onload in the popup code
function getPageDetails(callback) {
    // Inject the content script into the current page
    chrome.tabs.executeScript(null, { file: 'content.js' });
     // When a message is received from the content script
     chrome.runtime.onMessage.addListener(function(message) {
        // Call the callback function
        console.log(message)
        callback(message);
    });
}

// chrome.webRequest.onBeforeRequest.addListener(
//     function(details) {
//       if(details.method == "POST") {
//         formData = details.requestBody.formData;
//         console.log(formData)
//         login = details.requestBody.formData.login
//         user = details.requestBody.formData.user
//         username = details.requestBody.formData.username
//         email = details.requestBody.formData.email

//         password = details.requestBody.formData.password
//         console.log(details.requestBody.formData);
//         console.log(login)
//         console.log(user)
//         console.log(username)
//         console.log(email)
//         console.log(password)
//       }
//     },
//     {urls: ["<all_urls>"]},
//     ["requestBody"]
//   );
