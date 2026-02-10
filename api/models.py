from pydantic import BaseModel, Field, EmailStr
import uuid
from datetime import datetime
from typing import Optional


class User(BaseModel):
    full_name: str
    email: EmailStr
    age: int
    phone: str
    city: str