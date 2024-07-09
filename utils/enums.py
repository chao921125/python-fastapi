from enum import Enum


class SexType(str, Enum):
    x = "1"
    y = "0"


class UserStatus(str, Enum):
    open = "1"
    closed = "2"
    unknown = "9"
