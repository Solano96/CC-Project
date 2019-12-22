from portfolio_db import PortfolioDB

initial_user_doc = {
    '_id': 0,
    'dni': '00000000A',
    'saldo': 45,
    'acciones': {
        'AAPL': 10,
        'SAN': 20
    }
}

if __name__ == '__main__':
    database_info = PortfolioDB.get_db_collection('info')
    database_info.insert_one({'_id': 'users', 'value': 0})

    users_collection = PortfolioDB.get_users_collection()
    users_collection.insert_one(initial_user_doc)
