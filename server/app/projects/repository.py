from sqlalchemy import select
from app.base_repository import BaseRepository
from .models import Project
from app.database import engine
from sqlalchemy.orm import Session, selectinload

class ProjectsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Project)
    
    def get_by_id_detail(self, id):
        with Session(engine) as session:
            stmt = select(Project).options(selectinload(Project.client)).filter(Project.id == id)
            return session.scalars(stmt).first()