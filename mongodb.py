import pymongo
# from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import certifi

ca = certifi.where()

load_dotenv()  # take environment variables from .env.

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@cluster0.f8fgayr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
# client = MongoClient(uri)

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@cluster0.f8fgayr.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.get_database('test3').get_collection('rafa').insert_one(document={"marca": "opel", "modelo": "omega"})
client.get_database('test2').get_collection('andres').insert_one(document={"marca": "astra", "modelo": "chvrolet"})
