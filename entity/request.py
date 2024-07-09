from pydantic import BaseModel


class Request(BaseModel):
    id: str | int
    name: str
    age: int = 18
    sex: int = 1
    address: str = ""
    description: str = ""
