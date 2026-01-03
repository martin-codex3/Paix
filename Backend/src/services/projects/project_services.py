from sqlmodel.ext.asyncio.session import AsyncSession
from src.models.projects.project_model import ProjectModel
from src.schemas.products.product_schema import CreateProductSchema


class ProjectService:
    """the class will hold all the database functionality"""
    async def create_new_project(self, session: AsyncSession, project_data: CreateProductSchema):
        pass

    async def get_all_projects(self, session: AsyncSession):
        pass

    async def show_single_product(self, session: AsyncSession):
        pass

    async def update_project(self, session: AsyncSession, project_id: int):
        pass

    async def delete_project(self, session: AsyncSession, project_id: int):
        pass