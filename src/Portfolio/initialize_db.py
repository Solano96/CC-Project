from portfolio_db import PortfolioDB
import os

initial_user_doc_1 = {
    '_id': 0,
    'dni': '00000000A',
    'nombre': 'Nombre1',
    'saldo': 45,
    'acciones': {
        'AAPL': 10,
        'SAN': 20
    }
}

initial_user_doc_2 = {
    '_id': 1,
    'dni': '00000000B',
    'nombre': 'Nombre2',
    'saldo': 34,
    'acciones': {
        'BTC': 10,
        'SAN': 20,
        'GOOGL': 5
    }
}

if __name__ == '__main__':
    portfolio_database = PortfolioDB(db_name = 'Portfolio', db_uri = os.environ['DB_URI'])
    database_info = portfolio_database.get_info_collection()
    database_info.replace_one({'_id': 'users'}, {'_id': 'users', 'value': 1}, upsert=True)

    users_collection = portfolio_database.get_users_collection()
    users_collection.replace_one({'_id': 0}, initial_user_doc_1, upsert=True)
    users_collection.replace_one({'_id': 1}, initial_user_doc_2, upsert=True)
