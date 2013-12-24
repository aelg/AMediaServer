function playerCommand(cmd){
  xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", '/player/' + cmd, false);
  xmlHttp.send(null);
  return xmlHttp.response;
}
function update(){
  var info = JSON.parse(playerCommand('get_info'));
  //var info = {};
  if (typeof info.name != 'undefined'){
    var date = new Date(null);
    date.setSeconds(info.time);
    var s = '<p> Playing: ' + info.name + '</p>';
    s += '<p>Time: ';
    s += (date.getUTCHours()<10?'0':'') + date.getUTCHours() + ':';
    s += (date.getUTCMinutes()<10?'0':'') + date.getUTCMinutes() + ':';
    s += (date.getUTCSeconds()<10?'0':'') + date.getUTCSeconds();
    s += '</p>';
    document.getElementById('playerInfo').innerHTML = s;
  }
  else{
    document.getElementById('playerInfo').innerHTML = '<p>No video playing</p>';
  }
}
var timerId = 0;
function initPlayer(){
  update();
  timerId = window.setInterval(update, 1000);
}
