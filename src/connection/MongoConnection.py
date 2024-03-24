import os
from pymongo import MongoClient
from dotenv import load_dotenv

class MongoConnection:
    def __init__(self):
        load_dotenv()
        self.connection = self.set_mongo_connection()

    def set_mongo_connection(self):
        mongo_uri = f"mongodb://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DATABASE')}?authSource={os.getenv('MONGODB_AUTH_SOURCE')}"
        client = MongoClient(mongo_uri)
        db = client.get_default_database()

        return db
    
    def close_connection(self):
        self.connection.close()

    def insert_data(self, data):
        collection = self.connection.get_collection('sensor_data')
        try:
            id_inserido = collection.insert_one(data)
        except Exception as e:
            print(e)
            return None
        
        return self.get_inserted_data(id_inserido)
        
    def get_data(self, query):
        collection = self.connection.get_collection('sensor_data')
        return collection.find_one(query)
    
    def get_data_list(self, query):
        collection = self.connection.get_collection('sensor_data')
        return self.return_list(collection.find(query))
    
    def get_inserted_data(self, cursor):
        dados_inseridos = self.get_data({'_id': cursor.inserted_id})
        
        return dados_inseridos['sensores']
    
    def return_list(self, cursor):
        return [doc for doc in cursor]
        