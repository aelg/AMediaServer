from app.player import Player

class GlobalData(object):
  def __init__(self):
    self.player = Player()


globalData = GlobalData()
