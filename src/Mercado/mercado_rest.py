from flask import Flask, request
from flask_cors import CORS
from flask import Blueprint
from Mercado.mercado import Mercado

bp_quote = Blueprint('quote', 'quote', url_prefix='/quote')

mercado = Mercado

@bp_quote.route('/<symbol>', methods=['GET'])
def get_data(symbol):
    """
    Get finance data from symbol
    :param symbol: company symbol in yahoo finance
    :return: data in json format
    """
    return mercado.get_data(symbol)


@bp_quote.route('/realtime/<symbol>', methods=['GET'])
def get_data_in_realtime(symbol):
    return mercado.get_realtime_data(symbol)
