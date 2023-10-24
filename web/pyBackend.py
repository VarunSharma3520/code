from flask import Flask, jsonify

# Create a Flask app instance
app = Flask(__name__)


@app.route('/', methods=['GET'])
def login():
    data = {
        'username': 'febin'
        }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
