from pymongo import MongoClient

# Créer une connexion au client MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["fruits-visualisation"]
collection = db["fruits"]