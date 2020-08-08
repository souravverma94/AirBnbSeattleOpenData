from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
