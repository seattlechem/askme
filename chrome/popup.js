// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

function mouseDown(){
  console.log('yes')
  chrome.tabCapture.capture({audio: true}, (stream) => {
    let startTabId;
    chrome.tabs.query({active:true, currentWindow: true}, (tabs) => startTabId = tabs[0].id)
    const liveStream = stream;
    const audioCtx = new AudioContext();
    const source = audioCtx.createMediaStreamSource(stream);
    let mediaRecorder = new Recorder(source);
  })
}

function mouseUp(){
  console.log('stop')
  const stopCapture = function() {
    let endTabId;
    chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
      endTabId = tabs[0].id;
      if(mediaRecorder && startTabId === endTabId){
        mediaRecorder.stop();
        mediaRecorder.exportWAV((blob)=> {
          const audioURL = window.URL.createObjectURL(blob);
          const now = new Date(Date.now());
          const currentDate = now.toDateString();
          chrome.downloads.download({url: audioURL, filename: `${currentDate.replace(/\s/g, "-")} Capture`})
        })
      }});
    chrome.storage.sync.get({
      muteTab: false
    }, (options) => {
      if(!options.muteTab) {
        let audio = new Audio();
        audio.srcObject = liveStream;
        audio.play();
      }
    });
  };
}
