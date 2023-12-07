from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from src.auth.manager import get_user_manager
from src.auth.models import User
from src.config import SECRET_AUTH

cookie_transport = CookieTransport(cookie_name='shop', cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    """
    Определяет, как создавать и проверять JWT-токены.
    Он использует секретный ключ (SECRET_AUTH) для подписи токенов и время жизни токена (3600 секунд)."""
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)


auth_backend = AuthenticationBackend( # AuthenticationBackend - это класс, который связывает стратегию аутентификации (JWTStrategy) с транспортом (cookie_transport).
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,

    )

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# это декоратор, который позволяет получить текущего аутентифицированного пользователя в запросе.
current_user = fastapi_users.current_user()
