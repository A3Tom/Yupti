from app.base_repository import BaseRepository
from .models import Client
from app.database import engine
from sqlalchemy.orm import Session

class ClientsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)
    
