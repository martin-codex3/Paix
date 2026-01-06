from sqlmodel.ext.asyncio.session import AsyncSession
from src.models.projects.project_model import ProjectModel
from sqlmodel import select, desc, delete
from src.schemas.products.product_schema import (CreateProjectSchema,
                                                 FetchProjectSchema,
                                                 UpdateProjectSchema)


class ProjectService:
    """the class will hold all the database functionality"""
    async def create_new_project(self, session: AsyncSession, project_data: CreateProjectSchema):
        new_project_dict = project_data.model_dump()
        new_project = ProjectModel(**new_project_dict)
        if new_project is not None:
            session.add(new_project)
            await session.commit()
            return new_project
        else:
            return None


    async def get_all_projects(self, session: AsyncSession):
        statement = select(ProjectModel).order_by(desc(ProjectModel.project_created_at))
        results = await session.exec(statement)
        return results.all()

    async def show_single_product(self, project_id: int, session: AsyncSession):
        statement = select(ProjectModel).where(ProjectModel.project_id == project_id)
        results = await session.exec(statement)
        return results.first()

    async def update_project(self, project_data: UpdateProjectSchema, session: AsyncSession, project_id: int):
        project = await self.show_single_product(
            project_id = project_id,
            session = session
        )

        if project is not None:
            project_to_update_dict = project_data.model_dump()
            for keys, values in project_to_update_dict.items():
                setattr(project, keys, values)
            await session.commit()
            return project
        else:
            return None



    async def delete_project(self, session: AsyncSession, project_id: int):
        project = await self.show_single_product(
            project_id = project_id,
            session = session
        )

        if project is not None:
            await session.delete(project)
            await session.commit()
            return {}
        else:
            return None

