from application import app, db
from flask import render_template, request, redirect, url_for

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def home():
    
    return render_template('index.html')