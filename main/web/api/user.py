from fastapi import Depends, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from main.common.configuration import Configuration
from main.common.dto.response import ResponseDto
from main import get_conf

from main.dto.user import CreateUserDto
from main.dto.item import CreateItemDto
from main.dao.user import UserDao

router = InferringRouter()


@cbv(router)
class UserAPI:
    config: Configuration = Depends(get_conf)
    user_dao: UserDao = Depends(UserDao)

    @router.post("/")
    async def create_user(self, user: CreateUserDto):
        db_user = self.user_dao.get_user_by_email(email=user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return ResponseDto.success(self.user_dao.create_user(user=user))

    @router.get("/")
    async def get_users(self, skip: int = 0, limit: int = 100):
        users = self.user_dao.get_users(skip=skip, limit=limit)
        return ResponseDto.success(users)

    @router.get("/{user_id}")
    async def get_user(self, user_id: int):
        user = self.user_dao.get_user(user_id=user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return ResponseDto.success(user)

    @router.post("/{user_id}/items/")
    async def create_item_for_user(self, user_id: int, item: CreateItemDto):
        items = self.user_dao.create_user_item(item=item, user_id=user_id)
        return ResponseDto.success(items)
