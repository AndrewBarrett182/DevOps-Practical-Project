from flask import Flask
import random

app = Flask(__name__)

@app.route('/ticket', methods = ['GET'])
def ticket():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    lottery_ticket = []
    for i in range(6):
        generate = random.choice(numbers)
        lottery_ticket.append(generate)
        numbers.remove(generate)
    return lottery_ticket

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5001)