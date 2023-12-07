from typing import Optional

from fastapi_users import schemas
from pydantic import field_validator, EmailStr, Field
from src.auth.utils import phone_number_regex, check_password_regex


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    phone_number: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str = Field(max_length=100)
    email: EmailStr
    phone_number: str
    password: str
    confirm_password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    @field_validator('phone_number')
    def validate_phone_number(cls, phone_number):
        if not phone_number_regex(phone_number):
            raise ValueError('Invalid phone number')
        return phone_number

    @field_validator('password')
    def validate_password(cls, password):
        if not check_password_regex(password):
            raise ValueError("Password has to be longer than 7 symbols, Latin only, at least 1 "
                             "uppercase character, at least 1 special character $%&!")
        return password

    @field_validator('confirm_password')
    def confirm_password(cls, confirm_password, info):
        if confirm_password != info.data['password']:
            raise ValueError("confirm_password doesn't match password")
        return confirm_password


class UserUpdate(schemas.BaseUserCreate):
    username: str = Field(max_length=100)
    email: EmailStr
    phone_number: str
    password: str
    confirm_password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    @field_validator('password')
    def validate_password(cls, password):
        if not check_password_regex(password):
            raise ValueError("Password has to be longer than 7 symbols, Latin only, at least 1 "
                             "uppercase character, at least 1 special character $%&!")
        return password

    @field_validator('confirm_password')
    def confirm_password(cls, confirm_password, info):
        if confirm_password != info.data['password']:
            raise ValueError("confirm_password doesn't match password")
        return confirm_password
