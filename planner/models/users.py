from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event
from beanie import Document, Link

class User(Document):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "username": "Fastapi",
                "events": [],
            }
        }


class TokenTesponse(BaseModel):
    access_token: str
    token_type: str