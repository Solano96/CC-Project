import pandas as pd
import json
from pymongo import MongoClient


class DataBase:
    db_name = 'portfolio'

    @classmethod
    def get_data_json(cls, collection_name, limit=None):
        """
        Get data from database in json format
        :param collection_name: name of the collection
        :param limit: max data
        :return: data in json format
        """
        result = cls.get_data(collection_name, limit)
        return json.dumps(list(result)[::-1])

    @classmethod
    def get_data_df(cls, collection_name, limit=None):
        """
        Get data from database in df format
        :param collection_name: name of the collection
        :param limit: max data
        :return: data in df format
        """
        result = cls.get_data(collection_name, limit)
        return pd.DataFrame(list(result)[::-1])

    @classmethod
    def get_data(cls, collection_name, limit=None):
        """
        Get data from database
        :param collection_name: name of the collection
        :param limit: max data
        :return: data query result
        """
        collection = cls.get_db_collection(collection_name)

        if limit is None:
            result = collection.find({}).sort([('_id', -1)])
        else:
            result = collection.find({}).sort([('_id', -1)]).limit(int(limit))

        return result

    @classmethod
    def get_db(cls):
        """
        Get database
        :return: database
        """
        client = MongoClient('localhost:27017')
        return client[cls.db_name]

    @classmethod
    def get_db_collection(cls, collection_name):
        """
        Get a collection from db_name database
        :param collection_name: name of the collection
        :return: collection
        """
        db = cls.get_db()
        return db[collection_name]
