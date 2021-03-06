import threading
from time import sleep
from subprocess import Popen,PIPE,STDOUT
from os.path import exists
import re

class OMXPlayer(threading.Thread):
  def __init__(self, filePath, parent):
    threading.Thread.__init__(self)
    self.filePath = filePath
    self.time = 0
    self.length = ''
    self.lastMessage = ''
    self.subtitleMessage = ''
    self.out = ''
    self.process = None
    self.running = False
    self.parent = parent

    self.start()

  def run(self):
    self.running = True
    if exists('/usr/bin/unbuffer'):
      self.process = Popen(['unbuffer', '-p', 'omxplayer', '-s', '-I', self.filePath], stdin=PIPE, stdout=PIPE, bufsize = 1, universal_newlines=True)
    else:
      self.process = Popen(['omxplayer', '-s', self.filePath], stdin=PIPE, stdout=PIPE, bufsize = 1, universal_newlines=True)
    
    try:
      while self.process.returncode == None:
        #sleep(0.01)
        if self.process.poll() != None: break
        b = self.process.stdout.readline()
        m = re.match(r'.*Duration:\s*([0-9:.]+),.*', b)
        if m:
          duration = m.group(1)
          a = duration.split(':')
          self.length = float(a[0])*3600 + float(a[1])*60 + float(a[2])
          continue
        m = re.match(r'M:\s*([0-9]+) ', b)
        if m:
          self.time = int(float(m.group(1))/1000000)
          continue
        m = re.match(r'[^M].*', b)
        if m:
          self.lastMessage = m.group(0)
        m = re.match(r'Subtitle.*', b)
        if m:
          self.subtitleMessage = m.group(0)
          continue
    except:
      if self.process :
        self.process.terminate()
      raise
    finally:
      self.running = False
      self.parent.childTerminated()

  def terminate(self):
    if self.process and self.running:
      self.process.terminate()
      self.process.wait()
      while self.running:
        sleep(0.1)

  def write(self, s):
    if self.process and self.running:
      self.process.stdin.write(s)
      self.process.stdin.flush()

  def stdin(self):
    if self.process and self.running:
      return self.process.stdin;
    else: return None

  def stdout(self):
    if self.process and self.process.running:
      return self.process.stdout;
    else: return None

