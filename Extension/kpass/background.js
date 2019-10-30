// This function is called onload in the popup code
function getPageDetails(callback) {
    // Inject the content script into the current page
    chrome.tabs.executeScript(null, { file: 'content.js' });
     // When a message is received from the content script
     chrome.runtime.onMessage.addListener(function(message) {
        // Call the callback function
        callback(message);
    });
}

chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
      if(details.method == "POST") {
        console.log(details.requestBody.formData);
      }
    },
    {urls: ["<all_urls>"]},
    ["requestBody"]
  );