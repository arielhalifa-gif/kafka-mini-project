from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from typing import Optional


class User(BaseModel):
    full_name: str
    email: str
    age: int
    phone: str
    city: str