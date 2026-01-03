from sqlalchemy import create_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from src.config.app_config import AppConfig

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