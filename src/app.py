from flask import Flask, request
from flask_cors import CORS
from flask import Blueprint
from Mercado.mercado_rest import bp_quote

app = Flask(__name__)
app.register_blueprint(bp_quote)
CORS(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
