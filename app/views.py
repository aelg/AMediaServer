from app import playHandles
from app import closeAll
from app import app
from subprocess import Popen
from subprocess import call
from os import walk
import json
import re
from flask import render_template

videoFile = 'videoList.dat'

def readVideos():
    global videoFile
    f = open(videoFile)
    return json.loads(f.read())

@app.route('/')
@app.route('/index')
def index():
    videos = map(lambda x: x['name'], readVideos())

    return render_template('index.html', videos = enumerate(videos))

@app.route('/update')
def update():
    global videoFile
    videoDirs = ['/home/aelg/']
    videos = []
    for v in videoDirs:
        for dirpath, dirnames, filenames in walk(v):
            for name in sorted(filenames):
                #print(name)
                if re.search(r"[.](avi|mpg|mpeg|mkv)$", name):
                    videos.append({'dir': dirpath, 'name' : name})

    f = open(videoFile, 'w')
    f.write(json.dumps(videos))
    f.close()
    return 'Updated videos\n' + str(videos)

@app.route('/play/<int:i>')
def play(i):
    global playHandles
    videos = readVideos()
    closeAll()

    p = Popen(['/usr/bin/omxplayer', videos[i]['dir'] + '/' + videos[i]['name']])
    playHandles.append(p)
    return render_template('play.html', name = videos[i]['name'])
    

@app.route('/stop')
def stop():
    closeAll()
    return render_template('stop.html')
