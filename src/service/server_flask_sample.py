from flask import request, Flask

app = Flask(__name__)


@app.route('/oi', methods=['POST'])
def hello_world():
    data = request.data
    return data, 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4569)
