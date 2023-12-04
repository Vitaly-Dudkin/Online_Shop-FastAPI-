from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.product.models import product


async def get_specific_products(product_name: str, session: AsyncSession = Depends(get_async_session)):
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
