from fastapi import APIRouter, status, HTTPException
from fastapi.params import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from starlette.responses import JSONResponse

from src.schemas.products.product_schema import CreateProjectSchema, UpdateProjectSchema
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
async def store(project_data: CreateProjectSchema, session: AsyncSession = Depends(app_session)):
    new_project = await project_service.create_new_project(
        session = session,
        project_data = project_data
    )

    if new_project is not None:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Project created successfully",
            }
        )

    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "message": "failed to create the project"
            }
        )


# getting a single project here
@project_routes.get("/{project_id}", status_code=status.HTTP_200_OK)
async def show(project_id: int, session: AsyncSession = Depends(app_session)):
    single_project = await project_service.show_single_product(
        project_id = project_id,
        session = session
    )

    if single_project is not None:
        return single_project
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Failed to fetch the record with that id"
        )


# for updating the record here
@project_routes.put("/{project_id}", status_code=status.HTTP_200_OK)
async def update(project_id: int, project_data: UpdateProjectSchema, session: AsyncSession = Depends(app_session)):
    project = await project_service.update_project(
        project_id = project_id,
        session = session,
        project_data = project_data
    )

    if project is not None:
        return project
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Failed to update the record"
        )


# for deleting the project here
@project_routes.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(project_id: int, session: AsyncSession = Depends(app_session)):
    project = await project_service.delete_project(
        project_id = project_id,
        session = session
    )

    if project is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail={"message": "Failed to delete the project"})
    else:
        return {}
