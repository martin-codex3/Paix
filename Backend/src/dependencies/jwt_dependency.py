import jwt
from sqlalchemy import false
import logging
from src.config.app_config import AppConfig
from datetime import datetime, timedelta, timezone

key = AppConfig.JWT_TOKEN_HEX
algorithm = AppConfig.JWT_HASHING_ALGORITHM

# we will attempt to generate a jwt token here
def encode_jwt_token(user_data: dict, refresh: bool = False, expiry: timedelta = None) -> str:
    payload = {
        "user": user_data,
        "exp": datetime.now() + (expiry if expiry is not None else timedelta(minutes=60)),
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
        decoded_token: str = jwt.decode(
            jwt=jwt_token,
            key=key,
            algorithms=[algorithm]
        )

        return decoded_token

    except jwt.PyJWTError as error:
        logging.error(error)
        return None
