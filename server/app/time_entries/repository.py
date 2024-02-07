from sqlalchemy import select
from app.base_repository import BaseRepository
from .models import TimeEntry
from app.database import engine
from sqlalchemy.orm import Session, selectinload

class TimeEntriesRepository(BaseRepository):
    def __init__(self):
        super().__init__(TimeEntry)