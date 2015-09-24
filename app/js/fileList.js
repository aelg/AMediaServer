
function getDirs(){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function(){
    if(xmlHttp.readyState == 4 && xmlHttp.status == 200){
      var dirList = JSON.parse(xmlHttp.responseText);
      addParentLinks(dirList);
      setDir(dirList);
    }
  }
  xmlHttp.open("GET", '/getDirs', true);
  xmlHttp.send(null);
}

function playIndex(index){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", '/play/' + index.toString(), true);
  xmlHttp.send(null);
}

function resize(){
  updateHidden();
  document.getElementById('fileList').style.bottom = document.getElementById('player').offsetHeight + 'px';
  document.getElementById('fileList').style.height = (document.getElementById('container').offsetHeight - document.getElementById('player').offsetHeight) + 'px';
}

function initFileList(){
  //var fileList = document.getElementById('fileList');
  getDirs();
  //setDir(dirList);
  //fileList.className = 'jumbotron';
  //resize();
  //document.body.onresize = resize;
}

function addParentLinks(tree, parent){
  tree.parent = parent;
  for(var i = 0; i < tree.dirs.length; ++i){
    addParentLinks(tree.dirs[i], tree);
  }
}

function setDirEventHandler(tree){
  if(tree){
    return function (){setDir(tree); return false;};
  }
  return function (){window.location='/update';};
}

function playFileEventHandler(file){
  return function (){playIndex(file.index); return false;};
}

function createCurrentFolder(tree){
  var elem = document.createElement('a');
  elem.className = 'list-group-item active';
  elem.innerHTML = tree.name? '<i class="fa fa-chevron-left"></i>&nbsp; '+tree.path:'Update Video List';
  elem.href='';
  elem.onclick=setDirEventHandler(tree.parent);
  return elem;
}

function createFolder(tree){
  var elem = document.createElement('a');
  elem.className = 'list-group-item list-group-item-success';
  elem.innerHTML = tree.name;
  elem.href='';
  elem.onclick=setDirEventHandler(tree);
  return elem;
}

function createFile(file){
  var elem = document.createElement('a');
  elem.className = 'list-group-item';
  elem.innerHTML = file.file;
  elem.href='';
  elem.onclick=playFileEventHandler(file);
  return elem;
}

function setDir(tree){
  if(!tree) return;
  var fileList = document.getElementById('fileList');
  fileList.innerHTML = '';
  fileList.className = 'list-group';
  fileList.appendChild(createCurrentFolder(tree));
  for(var i = 0; i < tree.dirs.length; ++i){
    fileList.appendChild(createFolder(tree.dirs[i]));
  }
  for(var i = 0; i < tree.files.length; ++i){
    fileList.appendChild(createFile(tree.files[i]));
  }
}
