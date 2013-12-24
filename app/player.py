from subprocess import Popen
from subprocess import PIPE
from app import globalData
from app.processControl import OMXPlayer
import os
import json
import re


class Player(object):
  def __init__(self):
    global globalData
    self.process = None
    self.path = ''
    self.name = ''
    self.isPlaying = False
    self.currentVideo = 0
    self.videoList = self.readVideos(globalData.config['videoListFile'])

  def readVideos(self, videoFile):
    try:
      f = open(videoFile)
    except FileNotFoundError:
      return '{}'
    return json.loads(f.read())

  def getVideoList(self):
    return self.videoList

  def findVideo(self, index):
    video = None
    curDir = self.videoList
    while(not video):
      for d in curDir['dirs']:
        if index >= d['start'] and index < d['end']:
          curDir = d
          break
      else:
        for v in curDir['files']:
          if v['index'] == index:
            video = v;
            break
        else:
          raise IndexError()
    return video

  def update(self):
    global globalData
    def traverse(startIndex, directory):
      res = {'start': startIndex, 'dirs': [], 'files' : []}
      for (dirpath,dirnames,filenames) in os.walk(directory):
        res['path'] = dirpath
        for d in sorted(dirnames):
          startIndex, dirs = traverse(startIndex, os.path.join(dirpath,d))
          if dirs['start'] == dirs['end'] : continue
          dirs['name'] = d
          res['dirs'].append(dirs)
        del dirnames[:]
        for f in sorted(filenames):
          if not re.search(r'.*\.(avi|mpeg|mpg|mkv)$', f): continue
          res['files'].append({'file': f, 'index': startIndex, 'path': dirpath})
          startIndex += 1
      res['end'] = startIndex
      return startIndex, res

    videoDirs = globalData.config['videoDirs']
    index = 0
    videos = {'start': index, 'dirs': [], 'files': [], 'path': '/'}
    for (name, v) in videoDirs.items():
      index, dirs = traverse(index, v)
      if dirs['start'] == dirs['end']: continue
      dirs['name'] = name
      videos['dirs'].append(dirs)

    self.videoList = videos
    f = open(globalData.config['videoListFile'], 'w')
    f.write(json.dumps(videos))
    f.close()

  def getCurrentVideo(self):
    return self.currentVideo

  def getCurrentPath(self):
    return self.path

  def getCurrentName(self):
    return self.name

  def getTime(self):
    if self.process:
      return self.process.time
    else: return 0

  def childTerminated(self):
    self.path = ''
    self.name = ''
    self.process = None

    if self.isPlaying:
      try:
        self.play(self.currentVideo + 1)
      except:
        pass

  def play(self, i):
    global globalData
    if self.process :
      self.stop()

    self.isPlaying = True

    video = self.findVideo(i)
    self.path = video['path']
    self.name = video['file']
    filePath = (self.path + '/' + self.name)
    self.process = OMXPlayer(filePath, self)
    self.currentVideo = i

  def stop(self):
    self.isPlaying = False
    if self.process: 
      self.process.terminate()
    self.path = ''
    self.name = ''

  def getOut(self):
    if self.process:
      return str(self.process.out)

  def getInfo(self):
    if self.process and self.process.running:
      return json.dumps({'name': self.name, 'time': self.process.time})
    else:
      return '{}'

  def pause(self):
    if self.process:
      self.process.write(' ')

  def short_forward(self):
    if self.process:
      self.process.write('\x1b[C')

  def long_forward(self):
    if self.process:
      self.process.write('\x1b[A')

  def short_backward(self):
    if self.process:
      self.process.write('\x1b[D')

  def long_backward(self):
    if self.process:
      self.process.write('\x1b[B')

  def next_video(self):
    try:
      self.play(self.currentVideo + 1)
    except:
      pass

  def prev_video(self):
    try:
      self.play(self.currentVideo - 1)
    except:
      pass
