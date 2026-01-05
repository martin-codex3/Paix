from fastapi import APIRouter, status, HTTPException, Depends
from src.services.users.user_service import UserService
from src.schemas.users.user_schema import SignUpUserSchema
from src.connection.app_connections import app_session
from sqlmodel.ext.asyncio.session import AsyncSession

# the routes for the users
user_routes = APIRouter()
user_services = UserService()


@user_routes.post("/", status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data:SignUpUserSchema, session: AsyncSession = Depends(app_session)):

    password = user_data.password
    password_confirmation = user_data.confirm_password

    user_exists = await user_services.check_if_user_exists(
        user_data = user_data,
        session = session
    )

    if password != password_confirmation:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={
            "message": "provided passwords do not match!"
        })

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



