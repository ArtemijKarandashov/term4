from flask import Flask
from flask_socketio import SocketIO

import os

app = Flask(__name__,static_folder=os.path.abspath("./static"))
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from app import routes, sockets