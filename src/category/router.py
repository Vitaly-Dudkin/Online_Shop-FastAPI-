from select import select

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import fastapi_users
from src.auth.models import User
from src.category.models import category
from src.database import get_async_session


current_user = fastapi_users.current_user(active=True)

router = APIRouter(
    prefix="/category",
    tags=["Category"]
)


@router.get("/")
async def get_specific_product(category_name: str, session: AsyncSession = Depends(get_async_session),
                               user: User = Depends(current_user)):
    return 'category'
