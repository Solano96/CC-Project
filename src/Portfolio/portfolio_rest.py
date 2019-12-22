from flask import Flask, request
from flask_cors import CORS
from flask import Blueprint
from Portfolio.portfolio import Portfolio

bp_portfolio = Blueprint('portfolio', 'portfolio', url_prefix='/portfolio')


@bp_portfolio.route("/<dni>", methods=['GET'])
def consultar_info_usuario(dni):
    user_portfolio = Portfolio(dni)
    return user_portfolio.consultar_datos_usuario()


@bp_portfolio.route("/<dni>/saldo", methods=['GET'])
def consultar_saldo(dni):
    user_portfolio = Portfolio(dni)
    return user_portfolio.consultar_saldo()


@bp_portfolio.route("/<dni>/acciones", methods=['GET'])
def consultar_acciones(dni):
    user_portfolio = Portfolio(dni)
    return user_portfolio.consultar_acciones()


@bp_portfolio.route("/<dni>/acciones/<mercado>", methods=['GET'])
def consultar_acciones_mercado(dni, mercado):
    user_portfolio = Portfolio(dni)
    return user_portfolio.consultar_acciones_mercado(mercado)
