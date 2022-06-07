# from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__)
# CORS(app)


@app.route('/ping/')
def ping():
    return jsonify({'ping': 'pong'})

@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    return "".join(reversed(random_string))



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4445)
