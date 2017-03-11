from app import app
from app import globalData
from os import path
import re
from flask import render_template
from flask import redirect
from flask import send_file
from flask import jsonify
from flask import send_from_directory

bootstrapFolder = 'static/bootstrap/dist/'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/assets/<path:filename>')
def send_assets(filename):
    return send_from_directory('assets/', filename)

@app.route('/js/fileList.js')
def fileList_js():
  return send_file('js/fileList.js')

@app.route('/js/player.js')
def player_js():
  return send_file('js/player.js')

@app.route('/css/bootstrap.min.css')
def bootstrap_css():
  return send_file(bootstrapFolder + 'css/bootstrap.min.css');

@app.route('/css/bootstrap-theme.min.css')
def bootstrap_theme_css():
  return send_file(bootstrapFolder + 'css/bootstrap-theme.min.css');

@app.route('/js/bootstrap.min.js')
def bootstrap_js():
  return send_file(bootstrapFolder + 'js/bootstrap.min.js');

@app.route('/css/default.css')
def default_css():
  return send_file('css/default.css')

@app.route('/img/trans.png')
def trans_img():
  return send_file('img/trans.png')

@app.route('/getDirs')
def getDirs():
  return jsonify(globalData.player.getVideoList())

@app.route('/update')
def update():
    global globalData
    globalData.player.update()
    return redirect('/')

@app.route('/play/<int:i>')
def play(i):
    global globalData
    globalData.player.play(i)
    return ''
    
@app.route('/player/stop')
def stop():
    global globalData
    globalData.player.stop()
    return ''

@app.route('/player/pause')
def pause():
    global globalData
    globalData.player.pause()
    return ''

@app.route('/player/short_forward')
def short_forward():
    global globalData
    globalData.player.short_forward()
    return ''

@app.route('/player/long_forward')
def long_forward():
    global globalData
    globalData.player.long_forward()
    return ''

@app.route('/player/short_backward')
def short_backward():
    global globalData
    globalData.player.short_backward()
    return ''

@app.route('/player/long_backward')
def long_backward():
    global globalData
    globalData.player.long_backward()
    return ''

@app.route('/player/next_video')
def next_video():
    global globalData
    globalData.player.next_video()
    return ''

@app.route('/player/prev_video')
def prev_video():
    global globalData
    globalData.player.prev_video()
    return ''

@app.route('/player/prev_subtitle')
def prev_subtitle():
    global globalData
    globalData.player.prev_subtitle()
    return ''

@app.route('/player/next_subtitle')
def next_subtitle():
    global globalData
    globalData.player.next_subtitle()
    return ''

@app.route('/player/toggle_subtitle')
def toggle_subtitle():
    global globalData
    globalData.player.toggle_subtitle()
    return ''

@app.route('/player/get_info')
def get_data():
    global globalData
    return globalData.player.getInfo()


@app.route('/debug')
def debug():
  global globalData
  return globalData.player.getOut()
