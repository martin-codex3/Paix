from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import EmailStr
from src.services.users.user_service import UserService
from src.schemas.users.user_schema import SignUpUserSchema, SignInUserSchema
from src.connection.app_connections import app_session
from sqlmodel.ext.asyncio.session import AsyncSession

# the routes for the users
user_routes = APIRouter()
user_services = UserService()


@user_routes.post("/create-account", status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data:SignUpUserSchema, session: AsyncSession = Depends(app_session)):

    password = user_data.password
    email = user_data.email

    user_exists = await user_services.check_if_user_exists(
        email = email,
        session = session
    )

    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={
            "message": "account with that email already exists!"
        })

    else:
        new_user = await user_services.create_user_account(
            user_data = user_data,
            session = session
        )

        return new_user


# route for logging in the users here
@user_routes.post("/sign-in", status_code=status.HTTP_200_OK)
async def login(user_data: SignInUserSchema, session: AsyncSession = Depends(app_session)):
    email: EmailStr = user_data.email
    password: str = user_data.password

    user_exists = await user_services.check_if_user_exists(
        email = email,
        session = session
    )

    # we have to verify the password here




