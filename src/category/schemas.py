from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    id: int
    name: str = Field(max_length=50)
    description: str
