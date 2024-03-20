from database import collection
import requests

response = requests.get("https://www.fruityvice.com/api/fruit/all")

if(response.status_code >= 400):
    raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")

fruits: list[dict] = response.json()

collection.insert_many(fruits)