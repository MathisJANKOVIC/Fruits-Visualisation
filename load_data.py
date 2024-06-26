from database import collection
import requests

def main():
    response = requests.get("https://www.fruityvice.com/api/fruit/all")

    if(response.status_code >= 400):
        raise Exception(f"API request failed with status code {response.status_code}")

    fruits: list[dict] = response.json()
    collection.delete_many({})
    collection.insert_many(fruits)