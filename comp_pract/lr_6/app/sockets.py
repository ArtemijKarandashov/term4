from flask import session, request
from flask_socketio import emit
from . import socketio
from PIL import Image
from io import BytesIO

import base64

@socketio.on('connect')
def handle_connect():
    session['sid'] = request.sid
    print(f'Client connected: {session['sid']}')


@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconected: {session['sid']}')


@socketio.on('upload_image')
def handle_image(data):

    filename = data['name']
    if not (filename.rpartition('.')[-1] == 'png'):
        emit('invalid_type', {'result':'Invalid filetype'},room = session['sid'])
        return None

    image_data = data['image'].split(',')[1]
    image = None

    image = Image.open(BytesIO(base64.b64decode(image_data)))
    width, height = image.size
    emit('send_size', {'width':width,'height':height},room = session['sid'])
     