from flask import Flask, request
from flask_cors import CORS
from flask import Blueprint
from Portfolio.portfolio import Portfolio

bp_portfolio = Blueprint('portfolio', 'portfolio', url_prefix='/portfolio')

portfolio = portfolio
