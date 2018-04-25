from pymongo import MongoClient
from faker import Faker
import time

def write_test():
    fake = Faker()
    client = MongoClient("mongodb+srv://atlas:testAtlas@cluster1-o0ium.mongodb.net/test")
    db = client.get_database("failover")
    collection = db.get_collection("failover")
    while True:
        collection.insert_one({
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "intro": fake.text()
        })
        print("1 document inserted!")
        time.sleep(1)