import pandas as pd
import json
from pymongo import MongoClient


class PortfolioDB:

    def __init__(self, db_name = 'Portfolio', db_uri = 'localhost:27017'):
        self.client = MongoClient(db_uri)
        self.users_collection = self.client[db_name]['users']
        self.info_collection = self.client[db_name]['info']


    def get_users_collection(self):
        return self.users_collection


    def get_info_collection(self):
        return self.info_collection


    def get_user_portfolio(self, user_dni):
        result = self.users_collection.find({'dni': user_dni})
        return list(result)


    def __get_sequence(self, name):
        document = self.info_collection.find_one_and_update({"_id": name}, {"$inc": {"value": 1}}, return_document=True)
        return document["value"]


    def update_user_portfolio(self, portfolio):
        key = {'_id': portfolio['_id']}
        self.users_collection.replace_one(key, portfolio, upsert=True)
        return True


    def create_new_portfolio(self, user_dni, user_name):
        user_doc = {
            '_id': self.__get_sequence('users'),
            'dni': user_dni,
            'nombre': user_name,
            'saldo': 0,
            'acciones': {}
        }
        self.users_collection.insert_one(user_doc)
        return user_doc
