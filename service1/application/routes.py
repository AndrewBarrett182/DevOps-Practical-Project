from application import app, db
from flask import render_template, request
from application.models import Form
import requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        name = requests.get('http://service2:5001/name').text
        return render_template('index.html', form=form, name=name)
    
    return render_template('index.html', form=form)