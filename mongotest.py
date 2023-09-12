import pymongo
from pymongo.mongo_client import MongoClient

uri = f"mongodb+srv://darroyo606:Darling123@cluster0.ij08aaa.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
import certifi

ca = certifi.where()

client = pymongo.MongoClient(
    "mongodb+srv://darroyo606:Darling123@cluster0.ij08aaa.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.get_database('prueba').get_collection('rafa').insert_one(document={"marca": "opel", "modelo": "omega"})
