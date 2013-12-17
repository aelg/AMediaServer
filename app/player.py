from subprocess import Popen
from subprocess import PIPE

class Player(object):
  def __init__(self):
    self.process = None
    self.path = ''

  def play(self, filePath):
    if self.process :
      self.stop()

    self.process = Popen(['/usr/bin/omxplayer', filePath], stdin=PIPE, stdout=PIPE)
    self.path = filePath

  def stop(self):
    if self.process : 
      self.process.terminate()
    self.path = ''

  def pause(self):
    if self.process:
      #self.process.stdin.write(bytes('\x1b\x5b\x41', 'UTF-8'))
      self.process.stdin.write(bytes(' ', 'UTF-8'))
      self.process.stdin.flush()

  def short_forward(self):
    if self.process:
      self.process.stdin.write(bytes('\x1b[C', 'UTF-8'))
      self.process.stdin.flush()

  def long_forward(self):
    if self.process:
      self.process.stdin.write(bytes('\x1b[A', 'UTF-8'))
      self.process.stdin.flush()

  def short_backward(self):
    if self.process:
      self.process.stdin.write(bytes('\x1b[D', 'UTF-8'))
      self.process.stdin.flush()

  def long_backward(self):
    if self.process:
      self.process.stdin.write(bytes('\x1b[B', 'UTF-8'))
      self.process.stdin.flush()
