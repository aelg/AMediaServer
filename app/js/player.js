function playerCommand(cmd){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", '/player/' + cmd, true);
  xmlHttp.send(null);
  return true;
}

function getInfo(){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function(){
    if(xmlHttp.readyState == 4 && xmlHttp.status == 200){
      var info = JSON.parse(xmlHttp.responseText);
      onInfo(info);
    }
  }
  xmlHttp.open("GET", '/player/get_info', true);
  xmlHttp.send(null);
  timerId = window.setTimeout(getInfo, 2000);
}


function onInfo(info){
  if (typeof info.name != 'undefined'){
    var date = new Date(null);
    date.setSeconds(info.time);
    playedPercent = (info.time/info.length)*100;
    playedPercent = playedPercent >= 100 ? 100 : playedPercent;

    var s = '<p> Playing: ' + info.name + '</p>';
    s += '<p class="toggle">Subtitles: ' + (info.subtitleOn?'On':'Off');
    s += ' index: ' + info.subtitleIndex + '/' + info.subtitleCount;
    s += '</p>';
    s += '<p class="toggle">Time: ';
    s += (date.getUTCHours()<10?'0':'') + date.getUTCHours() + ':';
    s += (date.getUTCMinutes()<10?'0':'') + date.getUTCMinutes() + ':';
    s += (date.getUTCSeconds()<10?'0':'') + date.getUTCSeconds();
    s += '</p>';
    s += '<div class="progress"><div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="' + playedPercent + '" aria-valuemin="0" aria-valuemax="100" style="width: ' + playedPercent + '%"></div></div>'
    
    document.getElementById('playerInfo').innerHTML = s;
  }
  else{
    var s = '<p>No video playing</p>';
    s += '<p>Last played video: ' + /[^\/]*$/.exec(info.lastPlayedVideo)[0] + '</p>';
    document.getElementById('playerInfo').innerHTML = s;
  }
  resize();
}
var timerId = 0;
function initPlayer(){
  getInfo();
}
var toggleHidden = false;
function toggleControls(event){
  if(['button', 'i'].indexOf(event.target.tagName.toLowerCase()) != -1) return;
  toggleHidden = !toggleHidden;
  elems = document.getElementsByClassName('toggle');
  var newDisplay = toggleHidden?'none':'block';
  for(var i = 0; i < elems.length; ++i){
    elems[i].style.display = newDisplay;
  }
  resize();
}
function updateHidden(){
  elems = document.getElementsByClassName('toggle');
  var newDisplay = toggleHidden?'none':'block';
  for(var i = 0; i < elems.length; ++i){
    elems[i].style.display = newDisplay;
  }
}
