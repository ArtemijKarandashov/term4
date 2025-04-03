from . import app
from flask import render_template, jsonify


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return jsonify({'author','1149920'})

@app.route('/size2json')
def size2json():
    return render_template('size2json.html')