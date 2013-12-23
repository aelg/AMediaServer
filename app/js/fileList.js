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
  if (event.target == this){
    if(this.children.length == 0){
      this.innerHTML = '- ' + this.dirList.name;

      addFiles(this);
    }
    else{
      this.innerHTML = '+ ' + this.dirList.name;
    }
  }
  return false;
}
function fileClick(event){
  playIndex(this.file.index)
    return false;
}
function addFiles(div){
  var t = div.dirList;
  for(var i = 0; i < t.dirs.length; ++i){
    var elem = document.createElement('div')
      elem.innerHTML = '+ ' + t.dirs[i].name;
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
