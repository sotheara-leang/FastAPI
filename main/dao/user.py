from fastapi import Depends
from sqlalchemy.orm import Session

from main.database import get_db
from main.model.user import User
from main.model.item import Item
from main.dto.user import CreateUserDto
from main.dto.item import CreateItemDto


class UserDao:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: CreateUserDto):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = User(email=user.email, hashed_password=fake_hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(Item).offset(skip).limit(limit).all()

    def create_user_item(self, item: CreateItemDto, user_id: int):
        db_item = Item(**item.dict(), owner_id=user_id)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
