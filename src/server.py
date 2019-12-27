from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Blueprint
from Mercado.mercado_rest import bp_quote
from Portfolio.portfolio_rest import bp_portfolio

puerto = '8000'
app = Flask(__name__)

# Porfolio endpoints
app.register_blueprint(bp_portfolio)

@app.route("/", methods=['GET'])
def portfolio_inicio():
    return Response("CC-Project-Trading - Simulador de bolsa", status=200)

# Mercado endpoints
# app.register_blueprint(bp_quote)
CORS(app)

if __name__ == '__main__':
    app.debug = True
    app.run(port=puerto)
