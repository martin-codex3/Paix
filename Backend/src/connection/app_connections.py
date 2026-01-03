from sqlalchemy import create_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from src.config.app_config import AppConfig
from sqlalchemy.orm.session import sessionmaker


# we will attempt to create the database engine here
async_database_engine = AsyncEngine(
    create_engine(
        url=AppConfig.DATABASE_URL,
        echo=True
    )
)

# we will create the database connection here
async def database_init():
    async with async_database_engine.begin() as connection:
        if connection:
            await connection.run_sync(SQLModel.metadata.create_all)
        else:
            connection.close()


# we will the session maker to get the session here
# we will use this as the dependency to get the global app session
async def app_session():
    Session = sessionmaker(
        bind=async_database_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session