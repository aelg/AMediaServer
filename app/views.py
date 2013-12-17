from app import app
from app import globalData
from subprocess import Popen
from subprocess import call
from os import walk,path
import json
import re
from flask import render_template

f = open('config.json')
config = json.loads(f.read())
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
    global config
    videoDirs = config['videoDirs']
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
    global globalData
    videos = readVideos()
    
    globalData.player.play(videos[i]['dir'] + '/' + videos[i]['name'])
    return render_template('play.html', name = videos[i]['name'])
    

@app.route('/player/stop')
def stop():
    stoppedVideo = path.basename(globalData.player.path)
    globalData.player.stop()
    return render_template('stop.html', stoppedVideo=stoppedVideo)

@app.route('/player/pause')
def pause():
    pausedVideo = path.basename(globalData.player.path)
    globalData.player.pause()
    return render_template('showMessage.html', message='Paused ' + pausedVideo)

@app.route('/player/short_forward')
def short_forward():
    pausedVideo = path.basename(globalData.player.path)
    globalData.player.short_forward()
    return render_template('showMessage.html', message='Paused ' + pausedVideo)

@app.route('/player/long_forward')
def long_forward():
    pausedVideo = path.basename(globalData.player.path)
    globalData.player.long_forward()
    return render_template('showMessage.html', message='Paused ' + pausedVideo)

@app.route('/player/short_backward')
def short_backward():
    pausedVideo = path.basename(globalData.player.path)
    globalData.player.short_backward()
    return render_template('showMessage.html', message='Paused ' + pausedVideo)

@app.route('/player/long_backward')
def long_backward():
    pausedVideo = path.basename(globalData.player.path)
    globalData.player.long_backward()
    return render_template('showMessage.html', message='Paused ' + pausedVideo)
