import json

class GlobalData(object):
  def __init__(self):
    self.player = None
    
    f = open('config.json')
    self.config = json.loads(f.read())

  def setPlayer(self,player):
    self.player = player
