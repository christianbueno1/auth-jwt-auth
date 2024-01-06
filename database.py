from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()

database = getenv("MONGO_DB")
mongo_url = getenv("MONGO_URL")
# client = MongoClient(mongo_url)

# #database
# db = client[database]
# #collection
# users = db["users"]

# #delete if exists
# users.delete_many({})

# user = {
#     "username": "tom",
#     "fullname": "Tom Smith",
#     "email": "tom@ibm.com",
#     "hashed_password": "password123",
#     "disabled": False,
# }

# users.insert_one(user)

# dbs = client.list_database_names()
# print(f"dbs: {dbs}")
# if database in dbs:
#     print(f"The database {database} exists.")
# else:
#     print(f"The database {database} does not exist.")
    

# collections = db.list_collection_names()
# print(f"collections: {collections}")

# cursor = users.find()
# print(f"cursor: {cursor}")
# for doc in cursor:
#     print(f"doc: {doc}")



def get_database():
    client = MongoClient(mongo_url)
    return client[database]