from database import get_database
from pprint import PrettyPrinter

printer = PrettyPrinter(indent=4)
collection_name = "users"
print('getting user')

def get_user(username: str):
    db = get_database()
    # if username in db:
    #     user_data = db[username]
    #     return UserInDB(**user_data)
    collection = db[collection_name]
    result = collection.find_one({"username": username})
    # pprint(f"result: {result}")
    return result

printer.pprint(f"get_user: {get_user('tom')}")