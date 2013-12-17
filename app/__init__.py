from flask import Flask
import atexit
from app.globalData import globalData

app = Flask(__name__)

def closePlayer():
    global globalData
    globalData.player.stop()

from app import views
atexit.register(closePlayer)

