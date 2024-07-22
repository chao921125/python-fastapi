from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str
    age: int
    password: str
    birth: str
