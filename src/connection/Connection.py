import os
from pymongo import MongoClient
from dotenv import load_dotenv

class Connection:
    def __init__(self):
        load_dotenv()
        self.connection = set_mongo_connection()

def set_mongo_connection():
    mongo_uri = f"mongodb://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DATABASE')}"
    client = MongoClient(mongo_uri)
    db = client.get_default_database()
    return db

def insert_data(self, data):
    collection = self.connection.get_collection('sensor_data')
    collection.insert_many(data)