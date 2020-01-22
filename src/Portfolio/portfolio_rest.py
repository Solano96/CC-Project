import os
from flask import Flask, request, jsonify
from flask import Blueprint
from Portfolio.portfolio import Portfolio
from Portfolio.portfolio_db import PortfolioDB
from Portfolio.portfolioException import PortfolioException

bp_portfolio = Blueprint('portfolio', 'portfolio', url_prefix='/portfolio')

db_uri = os.environ['DB_URI']
os.environ['DB_NAME_PORTFOLIO'] = 'Portfolio'

portfolio_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], db_uri)

@bp_portfolio.route("/", methods=['GET'])
def portfolio_inicio():
    return jsonify({'Microservicio': 'Portfolio'})


@bp_portfolio.route("/<dni>", methods=['GET'])
def consultar_info_usuario(dni):
    """
    Servicio para consultar la información de un usuario
    :param dni: dni del usuario
    :return: dni y nombre
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
        return jsonify(user_portfolio.consultar_datos_usuario()), 200
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404

@bp_portfolio.route("/<dni>/saldo", methods=['GET'])
def consultar_saldo(dni):
    """
    Servicio para consultar el saldo disponible en la cuenta de un usuario
    :param dni: dni del usuario
    :return: saldo disponible
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
        return jsonify(user_portfolio.consultar_saldo()), 200
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404


@bp_portfolio.route("/<dni>/acciones", methods=['GET'])
def consultar_acciones(dni):
    """
    Servicio para consultar las acciones que tiene compradas un usuario
    :param dni: dni del usuario
    :return: lista de mercados y número de acciones de dichos mercados
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
        return jsonify(user_portfolio.consultar_acciones()), 200
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404


@bp_portfolio.route("/<dni>/acciones/<mercado>", methods=['GET'])
def consultar_acciones_mercado(dni, mercado):
    """
    Servicio para consultar las acciones que un usuario tiene compradas
    sobre un mercado concreto
    :param dni: dni del usuario
    :param mercado: nombre del mercado a consultar
    :return: número de acciones que se disponen del mercado <nombre_mercado>
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404

    try:
        acciones = user_portfolio.consultar_acciones_mercado(mercado)
        return jsonify(acciones), 200
    except PortfolioException:
        return jsonify({'error': 'mercado {} no encontrado.'.format(mercado)}), 404


@bp_portfolio.route('/<dni>/ingresar-saldo', methods=['POST'])
def ingresar_saldo(dni):
    """
    Servicio para ingresar saldo en el portfolio de un usuario
    :param dni: dni del usuario
    :return: saldo final tras realizar la operación
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404

    content = request.json
    user_portfolio.incrementar_saldo(content['cantidad'])
    return jsonify(user_portfolio.consultar_saldo())


@bp_portfolio.route('/<dni>/retirar-saldo', methods=['POST'])
def retirar_saldo(dni):
    """
    Servicio para retirar saldo del portfolio de un usuario
    :param dni: dni del usuario
    :return: saldo final tras realizar la operación
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404

    content = request.json

    try:
        user_portfolio.decrementar_saldo(content['cantidad'])
    except PortfolioException:
        return jsonify({'error': 'no se puede retirar más saldo del disponible.'}), 400

    return jsonify(user_portfolio.consultar_saldo())


@bp_portfolio.route('/<dni>/comprar-acciones', methods=['POST'])
def comprar_acciones(dni):
    """
    Servicio que permite comprar acciones desde la cuenta de un usuario
    :param dni: dni del usuario
    :return: lista de todas las acciones compradas tras realizar la operación
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404

    content = request.json

    try:
        user_portfolio.comprar_acciones_mercado(content['symbol'], content['cantidad'])
    except PortfolioException:
        return jsonify({'error': 'saldo insuficiente para comprar el número de acciones indicado.'}), 400

    return jsonify(user_portfolio.consultar_acciones())


@bp_portfolio.route('/<dni>/vender-acciones', methods=['POST'])
def vender_acciones(dni):
    """
    Servicio que permite vender acciones desde la cuenta de un usuario
    :param dni: dni del usuario
    :return: lista de todas las acciones compradas tras realizar la operación
    """

    try:
        user_portfolio = Portfolio(portfolio_db, dni)
    except PortfolioException:
        return jsonify({'error': 'dni {} no encontrado en la base de datos.'.format(dni)}), 404

    content = request.json

    try:
        user_portfolio.vender_acciones_mercado(content['symbol'], content['cantidad'])
    except PortfolioException:
        return jsonify({'error': 'no puedes vender acciones de las que no dispones.'}), 400

    return jsonify(user_portfolio.consultar_acciones())
