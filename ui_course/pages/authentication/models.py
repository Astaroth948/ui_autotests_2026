from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    email: EmailStr = ''
    username: str = ''
    password: str = ''


class IncorrectUserModel(UserModel):
    email: str
