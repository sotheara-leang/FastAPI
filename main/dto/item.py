from typing import Optional

from pydantic import BaseModel


class ItemDto(BaseModel):
    title: str
    description: Optional[str] = None


class CreateItemDto(ItemDto):
    pass


class ItemDetailDto(ItemDto):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
