from flask import Flask, request, jsonify
from flask import Blueprint
from Mercado.mercado import Mercado
from Mercado.mercadoException import MercadoException

bp_quote = Blueprint('quote', 'quote', url_prefix='/quote')

mercado = Mercado


@bp_quote.route("/", methods=['GET'])
def portfolio_inicio():
    return jsonify({'Microservicio': 'Mercado'})


@bp_quote.route('/<symbol>', methods=['GET'])
def get_data(symbol):
    """
    Servicio para obtener histórico de datos de un mercado
    :param symbol: símbolo del mercado correspondiente
    :return: histórico del mercado
    """

    try:
        return mercado.get_data(symbol)
    except MercadoException:
        return jsonify({'error': 'nombre de mercado incorrecto'}), 404


@bp_quote.route('/realtime/<symbol>', methods=['GET'])
def get_data_in_realtime(symbol):
    """
    Servicio para obtener información en tiempo real del mercado
    :param symbol: símbolo del mercado correspondiente
    :return: información del mercado en tiempo real
    """
    try:
        return mercado.get_realtime_data(symbol)
    except MercadoException:
        return jsonify({'error': 'nombre de mercado incorrecto'}), 404
