from app import app
from app import globalData
from os import path
import re
from flask import render_template
from flask import redirect
from flask import send_file
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/js/fileList.js')
def fileList_js():
  return send_file('js/fileList.js')

@app.route('/js/player.js')
def player_js():
  return send_file('js/player.js')

@app.route('/css/default.css')
def default_css():
  return send_file('css/default.css')

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
    return redirect('/player')
    
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

@app.route('/player/get_info')
def get_data():
    global globalData
    return globalData.player.getInfo()


@app.route('/debug')
def debug():
  global globalData
  return globalData.player.getOut()
