function playIndex(index){
  xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", '/play/' + index.toString(), false);
  xmlHttp.send(null);
  return false;
}
function getDirs(){
  xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", '/getDirs', false);
  xmlHttp.send(null);
  return JSON.parse(xmlHttp.response);
}
function folderClick(event){
  if(typeof this.expanded == 'undefined' || this.expanded == false){
    this.innerHTML = '<div class="icon">- </div><div class="folderName">' + this.dirList.name + '</div>';
    this.expanded = true;
    addFiles(this);
  }
  else{
    this.innerHTML = '<div class="icon">+ </div><div class="folderName">' + this.dirList.name + '</div>';
    this.expanded = false;
  }
  event.stopPropagation();
  return false;
}
function fileClick(event){
  playIndex(this.file.index)
  event.stopPropagation();
  return false;
}
function addFiles(div){
  var t = div.dirList;
  for(var i = 0; i < t.dirs.length; ++i){
    var elem = document.createElement('div')
      elem.innerHTML = '<div class="icon">+ </div><div class="folderName">' + t.dirs[i].name + '</div>';
    elem.onclick = folderClick;
    elem.dirList = t.dirs[i];
    elem.className = "folder"
      div.appendChild(elem);
  }
  for(var i = 0; i < t.files.length; ++i){
    var elem = document.createElement('div')
      elem.innerHTML = t.files[i].file;
    elem.onclick = fileClick;
    elem.file = t.files[i];
    elem.className = "file"
      div.appendChild(elem);
  }
}
var folder;
function initFileList(){
  var fileList = document.getElementById('fileList');
  fileList.dirList = getDirs();
  fileList.className = 'folder';
  addFiles(fileList);
}
