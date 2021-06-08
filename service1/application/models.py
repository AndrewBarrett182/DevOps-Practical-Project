from application import db
from flask_wtf import FlaskForm
from wtforms import SubmitField

class LotteryTickets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ticket = db.Column(db.String(50), nullable = False)
    winning = db.Column(db.String(50), nullable = False)
    prize = db.Column(db.Integer, nullable = False)

class Form(FlaskForm):
    generate = SubmitField("Generate")