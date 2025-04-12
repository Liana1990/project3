from pydantic import BaseModel, EmailStr


class UserSignUpSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserChangeUsernameSchema(BaseModel):
    user_id: int
    new_username: str

