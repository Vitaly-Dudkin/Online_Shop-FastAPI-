from fastapi import APIRouter, Depends, HTTPException
from src.auth.base_config import fastapi_users
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from .models import product
from .schemas import ProductCreate
from ..auth.models import User

router = APIRouter(
    prefix="/products",
    tags=["Product"]
)
current_user = fastapi_users.current_user(active=True)


@router.get("/")
async def get_specific_product(product_name: str, session: AsyncSession = Depends(get_async_session),
                               user: User = Depends(current_user)):
    try:

        query = select(product).where(product.c.name == product_name)
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
async def add_specific_product(new_product: ProductCreate, session: AsyncSession = Depends(get_async_session),
                               user: User = Depends(current_user)):
    stmt = insert(product).values(**new_product.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
