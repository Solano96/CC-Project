import pytest
import sys
import json
import os

sys.path.append('src')

from Portfolio.portfolio import Portfolio
from Portfolio.portfolioException import PortfolioException
from Portfolio.portfolio_db import PortfolioDB
from Portfolio.server import app


def init_portfolio_test():
    portfolio_test_db = PortfolioDB(os.environ['DB_NAME_PORTFOLIO'], os.environ['DB_URI'])

    database_info = portfolio_test_db.get_info_collection()
    key = {'_id': 'users'}
    doc = {'_id': 'users', 'value': 0}
    database_info.replace_one(key, doc, upsert=True)

    collection = portfolio_test_db.get_users_collection()
    collection.delete_many({'_id': {'$gt': 0}})

    portfolio_test_db.create_new_portfolio('12345678A', 'Nombre1')


@pytest.fixture
def client():
    init_portfolio_test()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_portfolio_inicio(client):
    ''' Test para comprobar que el servicio está funcionando '''

    response = client.get('/portfolio/')
    assert json.loads(response.data.decode("utf-8")) == {'Microservicio': 'Portfolio'}


def test_portfolio_dni(client):
    ''' Test asociados al DNI '''

    response = client.get('/portfolio/12345678A')
    assert json.loads(response.data.decode("utf-8")) == {'dni': '12345678A', 'nombre': 'Nombre1'}

    response = client.get('/portfolio/DNIINCORRECTO')
    assert response.status == '404 NOT FOUND'


def test_portfolio_saldo(client):
    ''' Tests asociados al saldo del cliente '''

    # Consultar saldo inicial
    response = client.get('/portfolio/12345678A/saldo')
    assert json.loads(response.data.decode("utf-8")) == {'saldo': 0}

    # Ingresar saldo
    response = client.post('portfolio/12345678A/ingresar-saldo', data=json.dumps({'cantidad': 25}), content_type='application/json')
    assert json.loads(response.data.decode("utf-8")) == {'saldo': 25}

    # Retirar saldo
    response = client.post('portfolio/12345678A/retirar-saldo', data=json.dumps({'cantidad': 10}), content_type='application/json')
    assert json.loads(response.data.decode("utf-8")) == {'saldo': 15}

    # Consultar saldo con DNI incorrecto
    response = client.get('/portfolio/DNIINCORRECTO/saldo')
    assert response.status == '404 NOT FOUND'

    # Ingresar saldo con DNI incorrecto
    response = client.post('portfolio/DNIINCORRECTO/ingresar-saldo', data=json.dumps({'cantidad': 25}), content_type='application/json')
    assert response.status == '404 NOT FOUND'

    # Retirar saldo con DNI incorrecto
    response = client.post('portfolio/DNIINCORRECTO/retirar-saldo', data=json.dumps({'cantidad': 10}), content_type='application/json')
    assert response.status == '404 NOT FOUND'

    # Retirar saldo con una cantidad superior a la disponible
    response = client.post('portfolio/12345678A/retirar-saldo', data=json.dumps({'cantidad': 100000}), content_type='application/json')
    assert response.status == '400 BAD REQUEST'


def test_portfolio_acciones(client):
    ''' Tests asociados a las acciones de la cartera del cliente '''

    # Consultar acciones en momento inicial
    response = client.get('/portfolio/12345678A/acciones')
    assert json.loads(response.data.decode("utf-8")) == {'acciones': {}}

    # Ingresar saldo (para poder comprar acciones)
    response = client.post('portfolio/12345678A/ingresar-saldo', data=json.dumps({'cantidad': 1000}), content_type='application/json')
    assert json.loads(response.data.decode("utf-8")) == {'saldo': 1000}


    # ----- RUTA: COMPRAR ACCIONES ----- #

    # Comprar acciones
    response = client.post('/portfolio/12345678A/comprar-acciones', data=json.dumps({'symbol': 'SAN', 'cantidad':10}), content_type='application/json')
    assert json.loads(response.data.decode("utf-8")) == {'acciones': {'SAN': 10}}

    # Comprar acciones
    response = client.post('/portfolio/12345678A/comprar-acciones', data=json.dumps({'symbol': 'SAN', 'cantidad':15}), content_type='application/json')
    assert json.loads(response.data.decode("utf-8")) == {'acciones': {'SAN': 25}}

    # Comprar acciones con DNI incorrecto
    response = client.post('/portfolio/DNIINCORRECTO/comprar-acciones', data=json.dumps({'symbol': 'SAN', 'cantidad':15}), content_type='application/json')
    assert response.status == '404 NOT FOUND'

    # Comprar acciones con menos dinero del necesario
    response = client.post('/portfolio/12345678A/comprar-acciones', data=json.dumps({'symbol': 'SAN', 'cantidad':15000}), content_type='application/json')
    assert response.status == '400 BAD REQUEST'

    # Vender acciones
    response = client.post('/portfolio/12345678A/vender-acciones', data=json.dumps({'symbol': 'SAN', 'cantidad':10}), content_type='application/json')
    assert json.loads(response.data.decode("utf-8")) == {'acciones': {'SAN': 15}}

    # Vender acciones con DNI incorrecto
    response = client.post('/portfolio/DNIINCORRECTO/vender-acciones', data=json.dumps({'symbol': 'SAN', 'cantidad':10}), content_type='application/json')
    assert response.status == '404 NOT FOUND'

    # Vender más acciones de las que se disponen
    response = client.post('/portfolio/12345678A/vender-acciones', data=json.dumps({'symbol': 'SAN', 'cantidad':10000}), content_type='application/json')
    assert response.status == '400 BAD REQUEST'

    # Consultar acciones de un mercado concreto
    response = client.get('/portfolio/12345678A/acciones/SAN')
    assert json.loads(response.data.decode("utf-8")) == {'SAN': 15}

    # Consultar acciones con DNI incorrecto
    response = client.get('/portfolio/DNIINCORRECTO/acciones')
    assert response.status == '404 NOT FOUND'

    # Consultar acciones de un mercado concreto con DNI incorrecto
    response = client.get('/portfolio/DNIINCORRECTO/acciones/SAN')
    assert response.status == '404 NOT FOUND'

    # Consultar acciones de un mercado incorrecto
    response = client.get('/portfolio/12345678A/acciones/NOEXISTE')
    assert response.status == '404 NOT FOUND'


def test_portfolio_create(client):
    ''' Test para comprobar el correcto funcionamiento de la creación de un portfolio '''

    response = client.post('/portfolio/', data=json.dumps({'user_dni': '00000000A', 'user_name': 'Name'}), content_type='application/json')
    assert json.loads(response.data.decode("utf-8")) == {'dni': '00000000A', 'nombre': 'Name'}
