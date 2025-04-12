from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from schemas import UserSignUpSchema, UserLoginSchema
from security import pwd_context, create_access_token

import main


users_auth_router = APIRouter(tags=["User Auth"])


@users_auth_router.post("/api/sign-up")
def sign_up(user_signup_data: UserSignUpSchema):
    name = user_signup_data.name
    email = user_signup_data.email
    password = user_signup_data.password

    hashed_password = pwd_context.hash(password)

    main.cursor.execute("""INSERT INTO users (name, email, password) VALUES (%s, %s, %s)""",
                        (name, email, hashed_password))
    main.conn.commit()

    return "OK"


@users_auth_router.post("/api/login")
def login(user_login_data: UserLoginSchema):
    email = user_login_data.email
    password = user_login_data.password


    main.cursor.execute("""SELECT * FROM users WHERE email=%s""",
                        (email,))

    user_from_db = main.cursor.fetchone()

    if user_from_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email '{email}' was not found!"
        )

    hashed_password_from_db = dict(user_from_db).get("password")

    if not pwd_context.verify(password, hashed_password_from_db):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Wrong password -> '{password}'"
        )

    user_data = {
        "email": email
    } # sa grum enq token sarqeluc

    token = create_access_token(user_data) # ays toxov kanchum enq create_access_token f-n , vori mej tvel enq useri tvjalner@. ays depqum email

    return token
