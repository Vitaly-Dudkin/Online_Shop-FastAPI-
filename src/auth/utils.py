from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.database import get_async_session
import re


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


def phone_number_regex(phone_number):
    """
    Функция проверяет, что номер начинается с "+7" и имеет длину 12 символов (10 цифр после "+7").
    :param phone_number:
    """
    pattern = r'^\+7\d{10}$'
    if re.match(pattern, phone_number):
        return True
    return False


def check_password_regex(password):
    """
    Функция проверяет, что пароль содержит как минимум одну заглавную букву,
     один из специальных символов ($, %, &, !) и имеет длину не менее 8 символов.
    :param password:

    """
    pattern = r'^(?=.*[A-Z])(?=.*[$%&!])[A-Za-z\d$%&!]{8,}$'
    if re.match(pattern, password):
        return True
    return False
