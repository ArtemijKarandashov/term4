from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def do_get():
    login = '1149920'
    dt = datetime.now()
    result = login + ',' + str(dt)
    return result

if __name__ == '__main__':
    app.run('127.0.0.1',8080) # aka serve_forever()
