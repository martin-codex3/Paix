from passlib.context import CryptContext
from src.config.app_config import AppConfig


# we have to create the password context here
context = CryptContext(
    schemes=[AppConfig.PASSWORD_HASHING_SCHEME]
)

# having the password here
def hash_user_password(password_hash: str) -> str:
    password: str = context.hash(
        secret=password_hash,
        scheme=AppConfig.PASSWORD_HASHING_SCHEME
    )

    return password


def verify_password_hash(password: str, password_hash: str) -> bool:
    password: bool = context.verify(
        scheme=AppConfig.PASSWORD_HASHING_SCHEME,
        secret=password,
        hash=password_hash
    )

    return password