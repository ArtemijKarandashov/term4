from flask import Flask
from config import AppConfig
from flask_socketio import SocketIO

import os


app = Flask(__name__,static_folder=os.path.abspath("./static"))
app.config.from_object(AppConfig)
socketio = SocketIO(app)

data_path = str(app.config['DATA_DIR_PATH'])
if not os.path.exists(data_path):
    os.makedirs(data_path)


from app.tools.logger import Logger
app_logger = Logger()


from app import routes