from . import app, app_logger
from .controller.rates_manager import RatesManager
from .controller.auth_manager import AuthManager
from flask import render_template, request

logger = app_logger.logger

rates = RatesManager()

auth_manager = AuthManager()

@app.route('/', methods=['GET','POST'])
def charcode():
    if request.method == 'GET':
        charcode = request.args.get("charcode")

        if charcode == None:
            logger.info('No charcode provided.')
            return render_template('index.html', rates = rates.read())

        rates.update([charcode])
        return render_template('index.html', rates = rates.read())
    if request.method == 'POST':
        charcodes = request.form.get('charcodes')

        if charcodes == None:
            logger.info('No charcodes provided.')
            return render_template('index.html', rates = rates.read())
        
        rates.update(charcodes.replace(' ', '').split(','))

        return render_template('index.html', rates = rates.read())


@app.route('/api/signup/', methods=['POST'])
def signup():
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']

    auth_manager.register_user(login,password)
    return "Success"


@app.route('/api/signin/', methods=['POST'])
def signin():
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']

    auth_manager.login_user(login, password, 1)
    return f"{login} succesefuly logged in"


@app.route('/api/signout/', methods=['POST'])
def singout():
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']
    
    auth_manager.logout_user(login, password, 1)
    return f"{login} succesefuly logged out"