from pydantic import EmailStr
from sqlmodel.ext.asyncio.session import AsyncSession
from src.schemas.users.user_schema import SignUpUserSchema
from sqlmodel import select
from src.models.user.user_model import UserModel
from src.utils.password_management.password_manager import hash_user_password


class UserService:

    """this will get the user by the provided email here"""
    async def get_user_by_email(self, email: EmailStr, session: AsyncSession):
        statement = select(UserModel).where(UserModel.email == email)
        results = await session.exec(statement)

        user = results.first()
        return user


    async def check_if_user_exists(self, user_data: SignUpUserSchema, session: AsyncSession):
        email = user_data.email # we will get the user email from the input here
        user_exists = await self.get_user_by_email(email = email, session = session)

        # checking if the user exists here
        if user_exists:
            return True
        else:
            return False


    async def create_user_account(self, user_data: SignUpUserSchema, session: AsyncSession):
        user = user_data.model_dump() # we have to convert the data here to a dict
        # we have to pass all the dict key, values to the model here
        new_user = UserModel(**user)

        if user is not None:
            password = user_data.password
            confirm_password = user_data.confirm_password

            # we will hash both of the passwords here
            new_user.confirm_password = hash_user_password(confirm_password)
            new_user.password = hash_user_password(password)

            session.add(new_user)
            await session.commit()
            return new_user
        else:
            return None


