from flask import Flask
from config import AppConfig

import os


app = Flask(__name__,static_folder=os.path.abspath("./static"))
app.config.from_object(AppConfig)

data_path = str(app.config['DATA_DIR_PATH'])
if not os.path.exists(data_path):
    os.makedirs(data_path)


from app.tools.logger import Logger
app_logger = Logger()


from app.controller.rates_manager import RatesManager
rates_manager = RatesManager('rates.db')


from app import routes