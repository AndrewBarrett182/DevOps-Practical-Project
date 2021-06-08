from application import app, db
from flask import render_template, request
from application.models import Form
import requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        ticket = requests.get('http://service2:5001/ticket').text
        lottery = requests.get('http://service3:5002/lottery').text
        send = {'ticket':ticket, 'lottery':lottery}
        prize = requests.post("http://service4:5003/prize", json=send).json
        return render_template('index.html', form=form, ticket=ticket, lottery=lottery, prize=prize)
    
    return render_template('index.html', form=form)