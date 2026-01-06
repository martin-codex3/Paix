import jwt
from sqlalchemy import false
import logging
from src.config.app_config import AppConfig
from datetime import datetime, timedelta, timezone

key = AppConfig.JWT_TOKEN_HEX
algorithm = AppConfig.JWT_HASHING_ALGORITHM

# we will attempt to generate a jwt token here
def encode_jwt_token(user: dict, refresh: bool = False) -> str:
    payload = {
        "user": user,
        "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=3600),
        "refresh": refresh,
    }

    # we then have to pass the payload
    jwt_token: str = jwt.encode(
        key = key,
        algorithm = algorithm,
        payload = payload
    )

    return jwt_token


# we will attempt to decode the token here
def decode_jwt_token(jwt_token: str):
    try:
        decoded_token = jwt.decode(
            jwt=jwt_token,
            key=key,
            algorithms=[algorithm]
        )

        return decoded_token

    except jwt.PyJWTError as error:
        logging.error(error)
        return None
