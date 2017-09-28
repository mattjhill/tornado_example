from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/report')
def report():
    return 'hello from flask'
