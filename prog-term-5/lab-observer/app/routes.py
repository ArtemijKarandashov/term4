from . import app, app_logger, socketio
from .controller.rates_manager import RatesManager
from .controller.auth_manager import AuthManager
from flask import render_template, request
from flask_socketio import emit


logger = app_logger.logger

rates = RatesManager(db_name="rates.db")
auth = AuthManager()

connected_clients = {}

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

    auth.register_user(login,password)
    return "Success"


@app.route('/api/signin/', methods=['POST'])
def signin():
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']
    sid = request_data['sid']

    auth.login_user(login, password, sid)
    return f"{login} succesefuly logged in"


@app.route('/api/signout/', methods=['POST'])
def singout():
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']
    
    auth.logout_user(login, password, 1)
    return f"{login} succesefuly logged out"


@socketio.on('connect')
def handle_connect():
    user_id = request.sid
    connected_clients[user_id] = request.sid
    print(f'Client connected: {user_id}')
    emit('status', {'message': 'You are connected!'}, to=request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    user_id = request.sid
    if user_id in connected_clients:
        del connected_clients[user_id]
    print(f'Client disconnected: {user_id}')