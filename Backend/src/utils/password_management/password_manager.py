from passlib.context import CryptContext

# we have to create the password context here
context = CryptContext(

)

# having the password here
def hash_user_password(password_hash: str) -> str
