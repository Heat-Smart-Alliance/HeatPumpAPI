from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "Hello world!"