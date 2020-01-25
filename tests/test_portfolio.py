import pytest
import sys

sys.path.append('src')

from Portfolio.portfolio import Portfolio
from Portfolio.portfolioException import PortfolioException
from Portfolio.portfolio_db import PortfolioDB


def clean_portfolio_test(portfolio_test_db):
    '''
    Función para limpiar la base de datos del test
    '''
    database_info = portfolio_test_db.get_info_collection()
    key = {'_id': 'users'}
    doc = {'_id': 'users', 'value': 0}
    database_info.replace_one(key, doc, upsert=True)

    collection = portfolio_test_db.get_users_collection()
    collection.delete_many({'_id': {'$gt': 0}})


@pytest.fixture(scope='session')
def user_portfolio():
    portfolio_test_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], os.environ['DB_URI'])
    clean_portfolio_test(portfolio_test_db)
    portfolio_test_db.create_new_portfolio('12345678X', 'Nombre1')
    return Portfolio(portfolio_test_db, '12345678X')


def test_portfolio(user_portfolio):
    '''
    Función test de las operaciones asociadas al saldo del portfolio
    '''
    with pytest.raises(PortfolioException, match="Error: DNI no encontrado."):
        assert Portfolio(PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], os.environ['DB_URI']), '12345678A')

    assert user_portfolio.consultar_datos_usuario() == {'dni': '12345678X', 'nombre': 'Nombre1'}
    assert user_portfolio.consultar_saldo() == {'saldo': 0}


def test_saldo(user_portfolio):
    '''
    Función test de las operaciones asociadas al saldo del portfolio
    '''
    assert user_portfolio.consultar_saldo() == {'saldo': 0}
    assert user_portfolio.incrementar_saldo(10) == {'saldo': 10}
    assert user_portfolio.decrementar_saldo(3) == {'saldo': 7}
    assert user_portfolio.consultar_saldo() == {'saldo': 7}

    # Comprobación de que no es posible restar mas saldo del disponible
    with pytest.raises(PortfolioException) as excinfo:
        user_portfolio.decrementar_saldo(200)

    excinfo.match("Error: saldo inferior a la cantidad a substraer.")


def test_acciones(user_portfolio):
    '''
    Función test de las operaciones asociadas a las acciones compradas
    '''
    assert user_portfolio.incrementar_saldo(100000) == {'saldo': 100007}

    assert user_portfolio.consultar_acciones() == {'acciones': {}}
    assert user_portfolio.comprar_acciones_mercado('AAPL', 15) == {'AAPL': 15}

    assert user_portfolio.comprar_acciones_mercado('AAPL', 15) == {'AAPL': 30}
    assert user_portfolio.vender_acciones_mercado('AAPL', 10) == {'AAPL': 20}
    assert user_portfolio.consultar_acciones() == {'acciones': {'AAPL': 20}}

    assert user_portfolio.comprar_acciones_mercado('GOOGL', 15) == {'GOOGL': 15}

    assert user_portfolio.consultar_acciones_mercado('AAPL') == {'AAPL': 20}
    assert user_portfolio.consultar_acciones_mercado('GOOGL') == {'GOOGL': 15}

    with pytest.raises(PortfolioException, match="Error: No hay acciones compradas de este mercado."):
        assert user_portfolio.consultar_acciones_mercado('FB')

    with pytest.raises(PortfolioException, match="Error: No hay acciones compradas de este mercado."):
        assert user_portfolio.vender_acciones_mercado('FB', 20)

    with pytest.raises(PortfolioException, match="Error: no se pueden susbtraer más acciones de las que se disponen."):
        assert user_portfolio.vender_acciones_mercado('GOOGL', 30)
