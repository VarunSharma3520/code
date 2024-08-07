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

@app.route('/delete', methods=['DELETE'])
def delete():
    data = {
        'message': 'Deleted'
        }
    return jsonify(data)

#  write for posting also
@app.route('/posting', methods=['POST'])
def posting():
    data = {
        'message': 'Post'
        }
    return jsonify(data)

#  write a hello world for "/getting" also
@app.route('/getting', methods=['GET'])
def getting():
    data = {
        'message': 'Get'
        }
    return jsonify(data)

