import pytest
import sys
sys.path.append('Portfolio')

from portfolio import Portfolio
from portfolio import PortfolioException


def test_saldo_1():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    assert portfolio_1.consultar_saldo() == {'saldo': 1500}


def test_saldo_2():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.incrementar_saldo(35)
    assert portfolio_1.consultar_saldo() == {'saldo': 1535}


def test_saldo_3():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.decrementar_saldo(55)
    assert portfolio_1.consultar_saldo() == {'saldo': 1445}


def test_saldo_4():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.incrementar_saldo(15)
    portfolio_1.decrementar_saldo(26)
    assert portfolio_1.consultar_saldo() == {'saldo': 1489}


def test_saldo_exception_1():
    portfolio_1 = Portfolio('123123', 'Francisco', 100)

    with pytest.raises(PortfolioException) as excinfo:
        portfolio_1.decrementar_saldo(200)

    excinfo.match("Error: saldo inferior a la cantidad a substraer.")


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
    assert acciones_aapl == {'AAPL': 22}

    acciones_googl = portfolio_1.consultar_acciones_mercado('GOOGL')
    assert acciones_googl == {"GOOGL": 28}


def test_acciones_3():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)
    portfolio_1.aniadir_acciones_mercado('GOOGL', 22)
    portfolio_1.substraer_acciones_mercado('GOOGL', 13)
    portfolio_1.aniadir_acciones_mercado('GOOGL', 15)

    assert len(portfolio_1.consultar_acciones()) == 1

    acciones_googl = portfolio_1.consultar_acciones_mercado('GOOGL')

    assert acciones_googl == {"GOOGL": 24}


def test_acciones_exception_1():
    portfolio_1 = Portfolio('123123', 'Francisco', 1500)

    with pytest.raises(PortfolioException, match="Error: No hay acciones compradas de este mercado."):
        assert portfolio_1.consultar_acciones_mercado('AAPL')


def test_acciones_exception_2():
    portfolio_1 = Portfolio('123123', 'Francisco', 123)

    with pytest.raises(PortfolioException, match="Error: No hay acciones compradas de este mercado."):
        assert portfolio_1.substraer_acciones_mercado('AAPL', 20)


def test_acciones_exception_3():
    portfolio_1 = Portfolio('123123', 'Francisco', 123)
    portfolio_1.aniadir_acciones_mercado('GOOGL', 22)

    with pytest.raises(PortfolioException, match="Error: no se pueden susbtraer más acciones de las que se disponen."):
        assert portfolio_1.substraer_acciones_mercado('GOOGL', 30)
