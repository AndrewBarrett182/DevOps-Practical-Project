from application import app, db
from flask import render_template, request
from application.models import Form, LotteryTickets
import requests

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        ticket = requests.get('http://service2:5001/ticket').json()['lottery_ticket']
        lottery = requests.get('http://service3:5002/lottery').json()['winning_numbers']
        send = {'ticket':ticket, 'lottery':lottery}
        prize = requests.post("http://service4:5003/prize", json=send).json()

        previous_tickets = LotteryTickets.query.all()

        db.session.add(LotteryTickets(ticket = ticket, winning = lottery, prize = prize))
        db.session.commit()

        return render_template('index.html', form=form, ticket=ticket, lottery=lottery, prize=prize, previous_tickets = previous_tickets)
    
    return render_template('index.html', form=form)