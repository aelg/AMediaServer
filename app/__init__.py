from flask import Flask
import atexit

playHandles = []
app = Flask(__name__)

def closeAll():
    global playHandles
    for p in playHandles:
        p.terminate()
    playHandles = []

from app import views
atexit.register(closeAll)

