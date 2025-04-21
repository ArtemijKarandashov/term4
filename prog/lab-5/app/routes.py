from . import app, rates_manager, app_logger
from flask import render_template, request

logger = app_logger.logger

@app.route('/', methods=['GET','POST'])
def charcode():
    if request.method == 'GET':
        charcode = request.args.get("charcode")

        if charcode == None:
            logger.info('No charcode provided.')
            return render_template('index.html', rates = rates_manager.read())

        rates_manager.update([charcode])
        return render_template('index.html', rates = rates_manager.read())
    if request.method == 'POST':
        charcodes = request.form.get('charcodes')

        if charcodes == None:
            logger.info('No charcodes provided.')
            return render_template('index.html', rates = rates_manager.read())
        
        rates_manager.update(charcodes.replace(' ', '').split(','))

        return render_template('index.html', rates = rates_manager.read())