from flask import Flask
import atexit

app = Flask(__name__)

playHandles = []

def closeAll():
    global playHandles
    for p in playHandles:
        p.terminate()
    del playHandles[:]

from app import views
atexit.register(closeAll)

