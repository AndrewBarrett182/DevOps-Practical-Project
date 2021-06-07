from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/prize', methods=['POST'])
def prize():
    return 