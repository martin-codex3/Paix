from fastapi import FastAPI
from src.routes.projects.project_routes import project_routes
from contextlib import asynccontextmanager
from src.connection.app_connections import database_init
import logging

# the version for the api
app_api_version = "v1"

# the app life span here
@asynccontextmanager
async def app_life_span(app: FastAPI):
    await database_init()
    yield
    logging.warn("The app is shutting down here")

# the main app entry point here
app = FastAPI(
    version=app_api_version,
    title="App Backend",
    description="The backend will include all "
                "the functionality to handle the different app operations",
    lifespan=app_life_span
)

# registering the routes here
app.include_router(
    router=project_routes,
    prefix="/api/products",
    tags=["products"]
)