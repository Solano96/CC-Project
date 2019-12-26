from portfolio_db import PortfolioDB

initial_user_doc = {
    '_id': 0,
    'dni': '00000000A',
    'nombre': 'Nombre1',
    'saldo': 45,
    'acciones': {
        'AAPL': 10,
        'SAN': 20
    }
}

if __name__ == '__main__':
    portfolio_database = PortfolioDB(db_name = 'Portfolio', db_uri = 'localhost:27017')
    database_info = portfolio_database.get_info_collection()
    database_info.insert_one({'_id': 'users', 'value': 0})

    users_collection = portfolio_database.get_user_portfolio()
    users_collection.insert_one(initial_user_doc)
