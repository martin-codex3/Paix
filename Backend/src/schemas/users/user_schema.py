from pydantic import Field, EmailStr, BaseModel
from datetime import datetime

# for creating a new user account
class SignUpUserSchema(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    email: EmailStr = Field(min_length=1)
    password: str = Field(min_length=1)
    confirm_password: str = Field(min_length=1)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now())


# for logging in the user
class SignInUserSchema(BaseModel):
    email: EmailStr = Field(min_length=1)
    password: str = Field(min_length=1)