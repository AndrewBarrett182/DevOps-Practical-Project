from flask import Flask, request, jsonify

app = Flask(__name__)

prizes = [0, 1, 5, 10, 30, 100, 10000]

@app.route('/prize', methods=['POST'])
def prize():
    match = 0
    ticket = request.json['ticket']
    lottery = request.json['lottery']
    for i in range(len(ticket)):
        if ticket[i] in lottery:
            match = match + 1
    return jsonify(prizes[match])

if __name__ == '__main__': app.run(host='0.0.0.0', port = 5003)