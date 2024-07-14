from pydantic import BaseModel
from fastapi import Query


class Request(BaseModel):
    id: str | int
    name: str
    age: int = 18
    sex: int = 1
    email: str = Query(default="", max_length=10)
    address: str = Query(default="", max_length=100)
    description: str = Query(default="", max_length=100)
    desc: str = Query(default="", max_length=100, deprecated=True,)
