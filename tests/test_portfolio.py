import pytest
import sys

sys.path.append('src')

from Portfolio.portfolio import Portfolio
from Portfolio.portfolioException import PortfolioException
from Portfolio.portfolio_db import PortfolioDB


@pytest.fixture(scope='session')
def user_portfolio():
    portfolio_test_db = PortfolioDB(db_name = 'Portfolio_test')
    portfolio_test_db.create_new_portfolio('12345678X', 'Nombre1')
    return Portfolio('12345678X')


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


def test_portfolio(user_portfolio):
    '''
    Función test de las operaciones asociadas al saldo del portfolio
    '''
    clean_portfolio_test()

    with pytest.raises(PortfolioException, match="Error: DNI no encontrado."):
        assert Portfolio('12345678A')

    assert user_portfolio.consultar_datos_usuario() == {'dni': '12345678X', 'nombre': 'Nombre1'}
    assert user_portfolio.consultar_saldo() == {'saldo': 0}
