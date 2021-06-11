from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/lottery', methods = ['GET'])
def lottery():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    winning_numbers = random.sample(numbers, 6)
    winning_numbers.sort()
    return jsonify({'winning_numbers':winning_numbers})

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5002)