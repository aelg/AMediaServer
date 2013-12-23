from flask import Flask
import atexit
from app.global_data import GlobalData

app = Flask(__name__)

globalData = GlobalData()
from app.player import Player
globalData.setPlayer(Player())

def closePlayer():
    global globalData
    globalData.player.stop()

from app import views
atexit.register(closePlayer)

