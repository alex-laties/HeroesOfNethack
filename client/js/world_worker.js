var xhr;
xhr = new XMLHttpRequest();
xhr.open('GET', "/ajax/snapshot");
xhr.onreadystatechange = function () {
  if (xhr.readyState != 4)
  {
    if (xhr.status != 200)
    {
      alert("oh god i'm on fire!")
    }
    return
  }
  
  postMessage({world: xhr.responseText, worldID: 1});
};
xhr.send();