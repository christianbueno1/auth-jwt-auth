from database import db
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    fullname: str
    disabled: bool or None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)
