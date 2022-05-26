import json
import pymongo
from pymongo import MongoClient

def get_database():

    client = pymongo.MongoClient("mongodb+srv://<mongodb>:<WQTi7nI4BwnEek4R>@cluster0.m4bts.mongodb.net/?retryWrites=true&w=majority")

    # Create the database for our example (we will use the same database throughout the tutorial
    return client


def lambda_handler(event, context):
    
    data = event['data']
    print("Data:", data)
    # if 'text' not in data:
    #     logging.error("Validation Failed")
    #     raise Exception("Couldn't create the todo item.")
    
    # TODO implement
    client = get_database()
    db = client.weather
    collection = db.weather_collection
    print("Collection: ", collection)
    # weather.weather_collection

    for item in data:
        print("item: ", item)
        collection.insert_one(item)

    return {
        'statusCode': 200,
        'body': data
    }