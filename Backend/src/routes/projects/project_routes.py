from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.services.projects.project_services import ProjectService
from src.connection.app_connections import app_session


project_routes = APIRouter()
project_service = ProjectService()

# all the routes for the projects here
@project_routes.get("/", status_code=status.HTTP_200_OK)
async def index(session: AsyncSession = Depends(app_session)):
    all_projects = await project_service.get_all_projects(
        session = session
    )

    if all_projects is not None:
        return all_projects
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={
            "message": "error fetching records"
        })


@project_routes.post("/", status_code=status.HTTP_201_CREATED)
async def store(session: AsyncSession = Depends(app_session)):
    pass
