from sqlmodel import SQLModel, Field
from datetime import datetime

class UserModel(SQLModel, table = True):

    __tablename__ = "users"
    user_id: int = Field(default=None, primary_key=True)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
    confirm_password: str = Field(min_length=1)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now())