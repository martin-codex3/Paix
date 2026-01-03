from sqlmodel import SQLModel, Field
from datetime import datetime


class ProjectModel(SQLModel, table = True):

    __tablename__ = "projects"

    project_id: int = Field(primary_key=True, default=None)
    project_title: str = Field(index=True, min_length=1)
    project_description: str = Field(min_length=1)
    project_category: str = Field(min_length=1)
    project_version: str = Field(default="v1")
    project_created_at: datetime = Field(default=datetime.now())
    project_updated_at: datetime = Field(default=datetime.now())
