'use strict';

  console.log('sdfsdf');
  let but = document.getElementById('start')
  but.addEventListener('mousedown', function(){
    chrome.tabCapture.capture({audio: true}, (stream) => {
      let startTabId;
      chrome.tabs.query({active:true, currentWindow: true}, (tabs) => startTabId = tabs[0].id)
      const liveStream = stream;
      const audioCtx = new AudioContext();
      const source = audioCtx.createMediaStreamSource(stream);
      let mediaRecorder = new Recorder(source);
  })}).then((result) => {
    console.log(result);
    
  }).catch((err) => {
    console.log(err);
  })
