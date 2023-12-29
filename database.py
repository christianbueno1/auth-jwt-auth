from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

database = getenv("MONGO_DB")
mongo_url = getenv("MONGO_URL")
client = MongoClient(mongo_url)

#database
db = client[database]
#collection
users = db["users"]

user = {
    "username": "tom",
    "password": "password123",
    "email": "tom@ibm.com"
}

# users.insert_one(user)

dbs = client.list_database_names()
print(f"dbs: {dbs}")
if database in dbs:
    print(f"The database {database} exists.")
else:
    print(f"The database {database} does not exist.")
    

collections = db.list_collection_names()
print(f"collections: {collections}")
