from fastapi import FastAPI
from src.routes.projects.project_routes import project_routes

# the version for the api
app_api_version = "v1"

# the main app entry point here
app = FastAPI(
    version=app_api_version,
    title="App Backend",
    description="The backend will include all "
                "the functionality to handle the different app operations"
)

# registering the routes here
app.include_router(
    router=project_routes,
    prefix="/api/products",
    tags=["products"]
)