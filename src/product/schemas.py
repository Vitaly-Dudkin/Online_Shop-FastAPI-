from datetime import datetime

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    id: int
    category: int
    price: float = Field(ge=0)
    name: str = Field(max_length=50)
    description: str
    created_at: datetime
    updated_at: datetime
    is_active: bool
