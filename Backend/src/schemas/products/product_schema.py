from pydantic import BaseModel, Field
from datetime import datetime


# creating a new product schema here
class CreateProjectSchema(BaseModel):
    project_title: str = Field(min_length=1)
    project_description: str = Field(min_length=1)
    project_category: str = Field(min_length=1)
    project_version: str = Field(default="v1")
    is_complete: bool = Field(default=False)
    project_created_at: datetime = Field(default=datetime.now())
    project_updated_at: datetime = Field(default=datetime.now())


# for fetching all the products
class FetchProjectSchema(BaseModel):
    project_title: str = Field(min_length=1)
    project_description: str = Field(min_length=1)
    project_category: str = Field(min_length=1)
    project_version: str = Field(default="v1")
    is_complete: bool = Field(default=False)
    project_created_at: datetime = Field(default=datetime.now())
    project_updated_at: datetime = Field(default=datetime.now())