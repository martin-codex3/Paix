from sqlmodel import SQLModel, Field
from datetime import datetime

class UserModel(SQLModel, table = True):

    __tablename__ = "users"
    user_id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    username: str
    email: str = Field(unique=True)
    password: str
    confirm_password: str
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now())