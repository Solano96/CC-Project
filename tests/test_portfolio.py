import pytest
import sys
sys.path.append('src')

from Portfolio.portfolio import Portfolio
from Portfolio.portfolioException import PortfolioException
from Portfolio.portfolio_db import PortfolioDB

PortfolioDB.db_name = 'PortfolioTest'


def clean_portfolio_test():
    '''
    Función para limpiar la base de datos del test
    '''
    database_info = PortfolioDB.get_db_collection('info')
    key = {'_id': 'users'}
    doc = {'_id': 'users', 'value': 0}
    database_info.replace_one(key, doc, upsert=True)

    collection = PortfolioDB.get_users_collection()
    collection.delete_many({'_id': {'$gt': 0}})


def test_portfolio():
    '''
    Función test de las operaciones asociadas al saldo del portfolio
    '''
    clean_portfolio_test()

    with pytest.raises(PortfolioException, match="Error: DNI no encontrado."):
        assert Portfolio('12345678X')

    PortfolioDB.create_new_portfolio('12345678X', 'Nombre1')
    user_portfolio = Portfolio('12345678X')

    assert user_portfolio.consultar_datos_usuario() == {'dni': '12345678X', 'nombre': 'Nombre1'}
    assert user_portfolio.consultar_saldo() == {'saldo': 0}


def test_saldo():
    '''
    Función test de las operaciones asociadas al saldo del portfolio
    '''
    clean_portfolio_test()

    PortfolioDB.create_new_portfolio('12345678X', 'Nombre1')
    user_portfolio = Portfolio('12345678X')

    assert user_portfolio.consultar_saldo() == {'saldo': 0}
    assert user_portfolio.incrementar_saldo(10) == {'saldo': 10}
    assert user_portfolio.decrementar_saldo(3) == {'saldo': 7}
    assert user_portfolio.consultar_saldo() == {'saldo': 7}

    # Comprobacion de que no es posible restar mas saldo del disponible
    with pytest.raises(PortfolioException) as excinfo:
        user_portfolio.decrementar_saldo(200)

    excinfo.match("Error: saldo inferior a la cantidad a substraer.")


def test_acciones():
    '''
    Función test de las operaciones asociadas a las acciones compradas
    '''
    clean_portfolio_test()

    PortfolioDB.create_new_portfolio('12345678X', 'Nombre1')
    user_portfolio = Portfolio('12345678X')

    assert user_portfolio.consultar_acciones() == {'acciones': {}}
    assert user_portfolio.aniadir_acciones_mercado('AAPL', 15) == {'AAPL': 15}
    assert user_portfolio.aniadir_acciones_mercado('AAPL', 15) == {'AAPL': 30}
    assert user_portfolio.substraer_acciones_mercado('AAPL', 10) == {'AAPL': 20}
    assert user_portfolio.consultar_acciones() == {'acciones': {'AAPL': 20}}

    assert user_portfolio.aniadir_acciones_mercado('GOOGL', 15) == {'GOOGL': 15}

    assert user_portfolio.consultar_acciones_mercado('AAPL') == {'AAPL': 20}
    assert user_portfolio.consultar_acciones_mercado('GOOGL') == {'GOOGL': 15}

    with pytest.raises(PortfolioException, match="Error: No hay acciones compradas de este mercado."):
        assert user_portfolio.consultar_acciones_mercado('FB')

    with pytest.raises(PortfolioException, match="Error: No hay acciones compradas de este mercado."):
        assert user_portfolio.substraer_acciones_mercado('FB', 20)

    with pytest.raises(PortfolioException, match="Error: no se pueden susbtraer más acciones de las que se disponen."):
        assert user_portfolio.substraer_acciones_mercado('GOOGL', 30)
