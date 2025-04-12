import datetime
from fastapi.security.oauth2 import OAuth2PasswordBearer
from passlib.context import CryptContext
from fastapi import Depends
from jose import jwt

oauth2_schema=OAuth2PasswordBearer(tokenUrl="/api/login")# asum enq token@ stacvelu e loginic

JWT_SECRET_KEY = "WETRYHJLDSFKFLSFDHBFOHFIRNVFUIDBVIJDRNVDRUI"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
ACCESS_TOKEN_ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def create_access_token(user_data: dict):
    access_token_expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    user_data.update(
        {
            "exp": access_token_expire
        }
    )

    access_token = jwt.encode(user_data, JWT_SECRET_KEY, ACCESS_TOKEN_ALGORITHM)

    return access_token


def verify_access_token(token: str):
    user_data = jwt.decode(token,JWT_SECRET_KEY,algorithms=[ACCESS_TOKEN_ALGORITHM])
    return user_data

def get_current_user(token=Depends(oauth2_schema)):#stananq @ntacik userin
    user_data=verify_access_token(token)
    return user_data
