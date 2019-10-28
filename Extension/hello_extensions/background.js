console.log("working")

chrome.webRequest.onBeforeRequest.addListener(
    function(details) {

      console.log(details)
      if(details.method == "POST") {
        // console.log(details.requestBody.formData);
        // console.log(new Int8Array(details.requestBody.raw))
        // console.log(String.fromCharCode.apply(null, new Uint16Array(details.requestBody.raw)))
        let formData = details.requestBody.formData;
        console.log(formData)
        let cancel = false;
        console.log(formData.password)
        console.log(formData.user)
        console.log(formData.username)
        if(formData) {
          Object.keys(formData).forEach(key => {
            formData[key].forEach(value => {
              console.log("key: ",key)
              console.log("value: ",value)
            });
          });
        }
  
        return {cancel: cancel};
      }
    },
    {urls: ["<all_urls>"]},
    ["requestBody"]
  );