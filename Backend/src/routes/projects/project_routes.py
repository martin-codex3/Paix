from fastapi import APIRouter


project_routes = APIRouter()


# all the routes for the projects here
project_routes.get("/")
async def index():
    return {"message": "all the routes for the projects here"}