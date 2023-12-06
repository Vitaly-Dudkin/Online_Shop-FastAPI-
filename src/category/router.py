from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import fastapi_users
from src.auth.models import User
from src.category.models import category
from src.category.schemas import CategoryCreate
from src.database import get_async_session

current_user = fastapi_users.current_user(active=True)

router = APIRouter(
    prefix="/category",
    tags=["Category"]
)


@router.get("/")
async def get_categories(session: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_user)):
    try:
        query = select(category)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all()
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None
        })


@router.post("/")
async def add_specific_category(new_operation: CategoryCreate, session: AsyncSession = Depends(get_async_session),
                                user: User = Depends(current_user)):
    stmt = insert(category).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {
        "status": "success",
    }
