from flask import Flask
import names

app = Flask(__name__)

@app.route('/name')
def name():
    return names.get_full_name()

if __name__ == '__main__':
    app.run(host='0.0.0.0')