from flask import Flask,render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def do_get():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        login = request.form['login']
        time = request.form['time']
        write_data(login + ' ' + time)
        return 'Form sumbitted!'
    return 404


def write_data(data):
    with open('output/user_data.txt', mode='a') as file:
        dt = '[' + str(datetime.now()) + '] '
        result_string = dt + data + '\n'
        file.write(result_string)

if __name__ == '__main__':
    app.run('127.0.0.1',8080)
