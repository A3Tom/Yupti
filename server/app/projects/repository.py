from app.base_repository import BaseRepository
from .models import Project
from app.database import engine
from sqlalchemy.orm import Session

class ProjectsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Project)
    
    