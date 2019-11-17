import pytest
import sys
sys.path.append('Portfolio')

from portfolio import Portfolio

def test_saldo_1():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    assert portfolio_1.consultar_saldo() == 1500

def test_saldo_2():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.incrementar_saldo(35)
    assert portfolio_1.consultar_saldo() == 1535

def test_saldo_3():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.decrementar_saldo(55)
    assert portfolio_1.consultar_saldo() == 1445

def test_saldo_4():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.incrementar_saldo(15)
    portfolio_1.decrementar_saldo(26)
    assert portfolio_1.consultar_saldo() == 1489

def test_acciones_1():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    assert len(portfolio_1.consultar_acciones()) == 0

def test_acciones_2():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.aniadir_acciones_mercado('AAPL', 22)
    portfolio_1.aniadir_acciones_mercado('GOOGL', 13)
    portfolio_1.aniadir_acciones_mercado('GOOGL', 15)

    assert len(portfolio_1.consultar_acciones()) == 2

    acciones_aapl = portfolio_1.consultar_acciones_mercado('AAPL')

    assert acciones_aapl['mercado'] == 'AAPL'
    assert acciones_aapl['acciones'] == 22

    acciones_googl = portfolio_1.consultar_acciones_mercado('GOOGL')

    assert acciones_googl['mercado'] == "GOOGL"
    assert acciones_googl['acciones'] == 28

def test_acciones_3():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.aniadir_acciones_mercado('GOOGL', 22)
    portfolio_1.substraer_acciones_mercado('GOOGL', 13)
    portfolio_1.aniadir_acciones_mercado('GOOGL', 15)

    assert len(portfolio_1.consultar_acciones()) == 1

    acciones_googl = portfolio_1.consultar_acciones_mercado('GOOGL')

    assert acciones_googl['mercado'] == "GOOGL"
    assert acciones_googl['acciones'] == 24
