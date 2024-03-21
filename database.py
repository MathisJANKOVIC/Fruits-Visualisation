from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017/")

db = mongo_client.get_database("fruits-visualisation")
collection = db.get_collection("fruits")