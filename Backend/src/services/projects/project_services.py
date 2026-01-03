from sqlmodel.ext.asyncio.session import AsyncSession
from src.models.projects.project_model import ProjectModel
from sqlmodel import select, desc
from src.schemas.products.product_schema import (CreateProjectSchema,
                                                 FetchProjectSchema)


class ProjectService:
    """the class will hold all the database functionality"""
    async def create_new_project(self, session: AsyncSession, project_data: CreateProjectSchema):
        pass

    async def get_all_projects(self, session: AsyncSession):
        statement = select(ProjectModel).order_by(desc(ProjectModel.project_created_at))
        results = await session.exec(statement)
        return results.all()

    async def show_single_product(self, session: AsyncSession):
        pass

    async def update_project(self, session: AsyncSession, project_id: int):
        pass

    async def delete_project(self, session: AsyncSession, project_id: int):
        pass