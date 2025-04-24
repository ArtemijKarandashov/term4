from flask import Flask, render_template, request, Response
from flask_cors import CORS
from PIL import Image

import io

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def handle():
    return render_template('index.html')


@app.route('/login')
def login():
    return {'author':'1149920'}


@app.route('/makeimage', methods=['GET','POST'])
def handle_makeimage():
    width = 0
    height = 0

    if request.method == 'GET':
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))
    
    if request.method == 'POST':
        data = request.json
        width = int(data('width'))
        height = int(data('height'))
    
    if width < 1 or height < 1:
        return {'message':'Invalid image size'}
    
    img = Image.new(mode='RGB',size=(width,height), color='green')

    img_bytes_arr = io.BytesIO()
    img.resize((width,height)).save(img_bytes_arr,format='PNG')

    resp = Response('GenImage')
    resp.headers['Content-Type'] = 'image/png'
    resp.data = img_bytes_arr.getvalue() 

    return resp

app.run()
