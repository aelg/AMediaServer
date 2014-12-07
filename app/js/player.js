function playerCommand(cmd){
  xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", '/player/' + cmd, false);
  xmlHttp.send(null);
  return xmlHttp.response;
}
function update(){
  var info = JSON.parse(playerCommand('get_info'));
  if (typeof info.name != 'undefined'){
    var date = new Date(null);
    date.setSeconds(info.time);
    playedPercent = (info.time/info.length)*100;
    playedPercent = playedPercent >= 100 ? 100 : playedPercent;

    var s = '<p> Playing: ' + info.name + '</p>';
    s += '<p>Subtitles: ' + (info.subtitleOn?'On':'Off');
    s += ' index: ' + info.subtitleIndex + '/' + info.subtitleCount;
    s += '</p>';
    s += '<p>Time: ';
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
  timerId = window.setTimeout(update, 5000);
}
var timerId = 0;
function initPlayer(){
  update();
  timerId = window.setTimeout(update, 5000);
}
