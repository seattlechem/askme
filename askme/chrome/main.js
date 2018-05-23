'use strict';
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var circle = new Path2D();

function layout(){
  ctx.canvas.width  = window.innerWidth;
  ctx.canvas.height = window.innerHeight;
  var x = c.width / 2;
  var y = c.height / 2;
  var radius = Math.min(c.width, c.height) / 4;
  circle.arc(x, y, radius, 0, 2 * Math.PI);
  ctx.lineWidth = 15;
  ctx.rect(0, 0, c.width, c.height);
  ctx.fill();
  ctx.shadowOffsetX = 0;
  ctx.shadowOffsetY = 0;
  ctx.shadowBlur = 10;
  ctx.shadowColor = '#ffffee';
  
  if (is_touch_device()){
    console.log('Touch Enabled');
    var el=document.getElementById("touch");
    c.ontouchstart = function(e){
      startrecord();
    } 
    c.ontouchend = function(e){
      stoprecord();
    }
  }
  else{
    console.log('No Touch');
    c.onmousedown = function(e){
      startrecord();
    } 
    c.onmouseup = function(e){
      stoprecord();
    }
  }
}        
  
function draw(col){
  ctx.clearRect(0, 0, c.width, c.height);
  ctx.fill();
  ctx.strokeStyle = col;
  ctx.stroke(circle);
}

function log(data){
  console.log('logging...')
  console.log(data);
}

function is_touch_device() {
  return !!('ontouchstart' in window);
}


window.onload = function() {
  layout();
  setup();
};

window.onresize = function() {
  location.reload();
};

$(document).ready(function(){

   $('.notSelectable').disableSelection();

});
$.fn.extend({
    disableSelection: function() {
        this.each(function() {
            this.onselectstart = function() {
                return false;
            };
            this.unselectable = "on";
            $(this).css('-moz-user-select', 'none');
            $(this).css('-webkit-user-select', 'none');
        });
    }
});
