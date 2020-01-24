from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from flask import Blueprint
from Mercado.mercado_rest import bp_quote
from Portfolio.portfolio_rest import bp_portfolio
import os

puerto = os.environ['PORT']
app = Flask(__name__)

# Porfolio endpoints
app.register_blueprint(bp_portfolio)
# Mercado endpoints
app.register_blueprint(bp_quote)

@app.route("/")
def index():
    return jsonify({'message': 'CC-Project-Trading - Simulador de bolsa'}), 200

# CORS(app)

if __name__ == '__main__':
    app.debug = True
    app.run(port=puerto)
