from pymongo import MongoClient
import requests

response = requests.get("https://www.fruityvice.com/api/fruit/all")

if(response.status_code >= 400):
    raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")

fruits: list[dict] = response.json()

client = MongoClient("mongodb://localhost:27017/")

db = client["fruits-visualisation"]
collection = db["fruits"]

# Insérer les données dans la collection
collection.insert_many(fruits)