from fastapi import FastAPI, Depends

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate

from src.product.router import router as router_product

app = FastAPI(
    title="Online_Shop App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_product)

current_user = fastapi_users.current_user(active=True)
