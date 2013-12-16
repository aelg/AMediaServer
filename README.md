AMediaServer
============

Lightweight media server for Raspberry Pi running Arch Linux, using flask and omxplayer.

This is barely working, but if you're interested feel free to ask or help.

Setup

Make sure you got a raspberry pi running Arch with setuptools and virtualenv.py (do $ easy_install virtualenv) and omxplayer installed.

Setup flask, in the repo root do:
$ virtualenv flask
$ flask/bin/pip install flask

Open config.json and change the folders to be searched for videos.

Run the server.
$ ./run.py

You should be able to connect to port 8080 on your RPi goto http://raspPi:8080/update search folder for videos.
The go back to the first page http://raspPi:8080 to see a list of videos, click to play.
