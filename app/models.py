from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class User(BaseModel):
    """User represents a user in the API database"""
    # using the optional type allows for POST requests to omit id values
    id: Optional[UUID] = uuid4()
    email: str
    gender: Gender
    age: int
    birthday: str




