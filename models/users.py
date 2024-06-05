
from typing import Optional
from pydantic import BaseModel
# username, fullname, email, disabled, hashed_password

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: Optional[bool] = None
    # disabled: bool or None = None

class UserInDB(User):
    hashed_password: str

