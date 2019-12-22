from portfolio_db import PortfolioDB

if __name__ == '__main__':
    database_info = PortfolioDB.get_db_collection('info')
    database_info.insert_one({'_id': 'users', 'value': 0})

    PortfolioDB.create_new_portfolio('00000000A', 'Nombre1')
    PortfolioDB.create_new_portfolio('00000000B', 'Nombre2')
