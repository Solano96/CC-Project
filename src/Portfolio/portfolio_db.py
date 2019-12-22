import pandas as pd
import json
from pymongo import MongoClient


class PortfolioDB:
    db_name = 'Portfolio'


    @classmethod
    def get_db(cls):
        client = MongoClient('localhost:27017')
        return client[cls.db_name]


    @classmethod
    def get_db_collection(cls, collection_name):
        db = cls.get_db()
        return db[collection_name]


    @classmethod
    def get_users_collection(cls):
        return cls.get_db_collection('users')


    @classmethod
    def get_user_portfolio(cls, user_dni):
        users_collection = cls.get_users_collection()
        result = users_collection.find({'dni': user_dni})
        return list(result)


    @classmethod
    def __get_sequence(cls, name):
        collection = cls.get_db_collection('info')
        document = collection.find_one_and_update({"_id": name}, {"$inc": {"value": 1}}, return_document=True)

        return document["value"]

    @classmethod
    def update_user_portfolio(cls, portfolio):
        users_collection = cls.get_users_collection()
        key = {'_id': portfolio['_id']}
        users_collection.replace_one(key, portfolio, upsert=True)
        return True


    @classmethod
    def create_new_portfolio(cls, user_dni, user_name):
        users_collection = cls.get_users_collection()
        user_doc = {
            '_id': cls.__get_sequence('users'),
            'dni': user_dni,
            'nombre': user_name,
            'saldo': 0,
            'acciones': {}
        }
        users_collection.insert_one(user_doc)
        return user_doc
