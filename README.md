AMediaServer
============

Lightweight media server for Raspberry Pi running Arch Linux, using python3, flask and omxplayer.

This is barely working, but if you're interested feel free to ask or help.

Setup

Make sure you got a raspberry pi running Arch with `setuptools` and `virtualenv.py` (do `$ easy_install virtualenv`) and `omxplayer` installed.
If `unbuffer` from the `expect` package is installed it will be used to get better latency in the played time of the video in the player. It also seems that reading duration and subtitle information often fails without unbuffer.
```
pacman -S python-virtualenv omxplayer expect
```

Goto the root of the repo and do:
```
$ virtualenv3 flask
$ flask/bin/pip install flask
```
Open config.json and change the folders to be searched for videos.

Then run the server.
```
$ ./run.py
```

You should be able to connect to port 8080 on your RPi, goto `http://raspPi:8080`. You'll need to search the folder for videos, use the button *Update Video List*.
