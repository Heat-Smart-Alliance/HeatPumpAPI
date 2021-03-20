from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    data_input = request.json
    return jsonify(data_input)

@app.route('/test', methods=['GET'])
def test():
    return {'message': "Hello World"}

if __name__ == "__main__":
    app.run(debug=True)