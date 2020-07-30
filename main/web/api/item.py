from typing import List
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from fastapi import Depends

from main.dao.item import ItemDao
from main.dto.item import ItemDetailDto

router = InferringRouter()


@cbv(router)
class ItemAPI:
    
    item_dao: ItemDao = Depends(ItemDao)

    @router.get("/", response_model=List[ItemDetailDto])
    async def read_items(self, skip: int = 0, limit: int = 100):
        items = self.item_dao.get_items(skip=skip, limit=limit)
        return items
