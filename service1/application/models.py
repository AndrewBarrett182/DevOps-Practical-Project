from application import db
from flask_wtf import FlaskForm
from wtforms import SubmitField

class Form(FlaskForm):
    generate = SubmitField("Generate")