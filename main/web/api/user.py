from typing import List
from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from main.dto.user import CreateUserDto, UserDetailDto
from main.dto.item import CreateItemDto, ItemDetailDto
from main.dao.user import UserDao

router = InferringRouter()


@cbv(router)
class UserAPI:
    
    user_dao: UserDao = Depends(UserDao)

    @router.post("/", response_model=UserDetailDto)
    async def create_user(self, user: CreateUserDto):
        db_user = self.user_dao.get_user_by_email(email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return self.user_dao.create_user(user=user)

    @router.get("/", response_model=List[UserDetailDto])
    async def read_users(self, skip: int = 0, limit: int = 100):
        users = self.user_dao.get_users(skip=skip, limit=limit)
        return users

    @router.get("/{user_id}", response_model=UserDetailDto)
    async def read_user(self, user_id: int):
        db_user = self.user_dao.get_user(user_id=user_id)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

    @router.post("/{user_id}/items/", response_model=ItemDetailDto)
    async def create_item_for_user(self, user_id: int, item: CreateItemDto):
        return self.user_dao.create_user_item(item=item, user_id=user_id)
