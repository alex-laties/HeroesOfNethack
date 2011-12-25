var xhr;

function onmessage(event) {
  xhr = new XMLHttpRequest();
  xhr.open('GET', "http://www.aperaturetesting.com:8080/ajax/snapshot");
  xhr.onreadystatechange = function () {
    if (xhr.readyState ==4)
    {
      postMessage({world: xhr.responseText, worldID: 1});
    }
  };
  xhr.send();
}