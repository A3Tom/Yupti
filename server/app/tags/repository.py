from sqlalchemy import select
from app.base_repository import BaseRepository
from .models import Tag
from app.database import engine
from sqlalchemy.orm import Session, selectinload

class TagsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Tag)