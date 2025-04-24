from flask import Flask, render_template, request, Response
from flask_cors import CORS
from PIL import Image

import numpy as np
import io

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def handle():
    return render_template('index.html')


@app.route('/login')
def login():
    return '1149920'


@app.route('/makeimage', methods=['GET'])
def handle_makeimage():
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    
    img = Image.new(mode='RGB',size=(width,height), color='green')

    img_bytes_arr = io.BytesIO()
    img.resize((width,height)).save(img_bytes_arr,format='PNG')

    resp = Response('GenImage')
    resp.headers['Content-Type'] = 'image/png'
    resp.data = img_bytes_arr.getvalue() 

    return resp

app.run()