from typing import List

from pydantic import BaseModel
from main.dto.item import ItemDetailDto


class UserBase(BaseModel):
    email: str


class CreateUserDto(UserBase):
    email: str
    password: str

    
class UserDetailDto(UserBase):
    id: int
    is_active: bool
    items: List[ItemDetailDto] = []

    class Config:
        orm_mode = True

