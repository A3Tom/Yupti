from sqlalchemy.orm import Session
from app.common.base_repository import BaseRepository
from app.common.database import engine
from .models import Client

class ClientsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)
    
