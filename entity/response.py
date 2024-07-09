from pydantic import BaseModel


class Response(BaseModel):
    code: int = 0
    msg: str = ""
    data: None = None


def response(code: int = 0, msg: str = "", data: BaseModel | None = None):
    return {
        "code": code,
        "msg": msg,
        "data": data,
    }
