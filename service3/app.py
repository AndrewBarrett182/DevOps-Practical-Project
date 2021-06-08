from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/lottery', methods = ['GET'])
def lottery():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    winning_numbers = []
    for i in range(6):
        generate = random.choice(numbers)
        winning_numbers.append(generate)
        numbers.remove(generate)
    return jsonify(winning_numbers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5002)