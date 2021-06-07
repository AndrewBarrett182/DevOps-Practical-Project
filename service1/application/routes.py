from application import app, db
from flask import render_template, request
from application.models import Form
import requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = Form()
    if request.method == "POST":
        name = requests.get('http://service2:5000/name').text
        return f"{name}"
    
    return render_template('index.html', form=form)