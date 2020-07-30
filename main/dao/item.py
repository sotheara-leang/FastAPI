from fastapi import Depends
from sqlalchemy.orm import Session

from main.database import get_db
from main.model.item import Item


class ItemDao:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_items(self, skip: int = 0, limit: int = 100):
        return self.db.query(Item).offset(skip).limit(limit).all()
