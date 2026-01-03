from sqlmodel import SQLModel, Field
from datetime import datetime


class ProjectModel(SQLModel, table = True):

    __tablename__ = "projects"

    project_id: int = Field(primary_key=True, default=None)
    project_title: str = Field(index=True)
    project_description: str
    project_category: str
    project_version: str
    is_complete: bool = Field(default=False)
    project_created_at: datetime = Field(default=datetime.now())
    project_updated_at: datetime = Field(default=datetime.now())
