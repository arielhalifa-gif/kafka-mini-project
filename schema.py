from pydantic import BaseModel


class User(BaseModel):
    full_name: str
    email: str
    age: int
    phone: str
    city: str