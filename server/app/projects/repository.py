from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.common.database import engine
from app.common.base_repository import BaseRepository
from .models import Project

class ProjectsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Project)