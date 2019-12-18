from flask import Flask, request
from flask_cors import CORS
from flask import Blueprint
from mercado import Mercado

app = Flask(__name__)
CORS(app)

mercado = Mercado

@app.route('/<symbol>', methods=['GET'])
def get_data(symbol):
    """
    Get finance data from symbol
    :param symbol: company symbol in yahoo finance
    :return: data in json format
    """
    return mercado.get_data(symbol)


@app.route('/realtime/<symbol>', methods=['GET'])
def get_data_in_realtime(symbol):
    return mercado.get_realtime_data(symbol)


if __name__ == '__main__':
    app.debug = True
    app.run()
