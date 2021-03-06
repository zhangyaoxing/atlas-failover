from pymongo import MongoClient
from faker import Faker
import time
import sys

def write_test(isRetry):
    uri = "mongodb+srv://atlas:testAtlas@cluster1-o0ium.mongodb.net/test"
    if isRetry:
        uri += "?retryWrites=true"
        print('Retryable writes enabled!')
    client = MongoClient(uri)
    db = client.get_database("failover")
    adminDB = client.get_database("admin")
    collection = db.get_collection("failover")
    fake = Faker()
    while True:
        try:
            # Get replica set status
            members = adminDB.command('replSetGetStatus')['members']
            for m in members:
                if m['stateStr'] == 'PRIMARY':
                    print('Current primary: ' + m['name'])

            # Insert fake document
            doc = {
                "name": fake.name(),
                "address": fake.address(),
                "email": fake.email(),
                "intro": fake.text()
            }
            collection.insert_one(doc)
            print("1 document inserted! Email: " + doc['email'])
        except:
            print('Insert failed!', sys.exc_info()[0])
        finally:
            time.sleep(1)