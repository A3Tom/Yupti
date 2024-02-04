from app.database import engine
from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        with Session(engine) as session:
            return session.query(self.model).all()

    def get_by_id(self, id):
        with Session(engine) as session:
            return session.query(self.model).get(id)
        
    def delete(self, id):
        entity = self.get_by_id(id)

        if hasattr(entity, 'is_deleted'):
            entity.is_deleted = True
            with Session(engine) as session:
                session.commit()
        else:
            with Session(engine) as session:
                session.delete(entity)
                session.commit()

    def update(self, id, data):
        entity = self.get_by_id(id)

        for key, value in data.items():
            setattr(entity, key, value)

        with Session(engine) as session:
            session.commit()
        
        return entity
    
    def create(self, entity):
        with Session(engine) as session:
            session.add(entity)
            session.commit()
            return self.get_by_id(entity.id)        
    
    def deactivate(self, id):
        entity = self.get_by_id(id)

        if hasattr(entity, 'is_active'):
            entity.is_active = False
            with Session(engine) as session:
                session.commit()
        else:
            raise AttributeError(f"{self.model.__name__} does not have an is_active attribute")
        
        return entity