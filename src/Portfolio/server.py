from flask import Flask, request, jsonify, Response
from flask import Blueprint
from Portfolio.portfolio_rest import bp_portfolio
import os

app = Flask(__name__)

# Porfolio endpoints
app.register_blueprint(bp_portfolio)

@app.route("/")
def index():
    return jsonify({'message': 'CC-Project-Trading - Simulador de bolsa'}), 200

if __name__ == '__main__':
    app.debug = True
    app.run(host=os.environ['HOST_PORTFOLIO'], port=os.environ['PORT_PORTFOLIO'])
