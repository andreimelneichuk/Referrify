from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class ReferralCodeCreate(BaseModel):
    expiration_date: datetime

class UserResponse(BaseModel):
    id: int
    email: str

class ReferralCodeResponse(BaseModel):
    code: str
    expiration_date: datetime
