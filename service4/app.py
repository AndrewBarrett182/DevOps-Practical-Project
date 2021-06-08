from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/prize', methods=['POST'])
def prize():
    return 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5003)