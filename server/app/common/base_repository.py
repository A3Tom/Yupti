from sqlalchemy import select
from sqlalchemy import update
from app.database import engine
from sqlalchemy.orm import Session, selectinload

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        with Session(engine) as session:
            return session.query(self.model).all()
        
    def exists(self, id):
        with Session(engine) as session:
            return session.query(self.model).filter(self.model.id == id).count() > 0

    def get_by_id(self, id):
        with Session(engine) as session:
            return session.query(self.model).get(id)
        
    def get_by_id_detail(self, id):
        with Session(engine) as session:
            stmt = select(self.model).options(selectinload("*")).filter(self.model.id == id)
            return session.scalars(stmt).first()
        
    def delete(self, id):
        entity = self.get_by_id(id)

        if hasattr(entity, 'is_deleted'):
            entity.is_deleted = True    # Todo: replace this with same logic as in update statement
            with Session(engine) as session:
                session.commit()
        else:
            with Session(engine) as session:
                session.delete(entity)
                session.commit()
                
        return True

    def update(self, id, data):
        statement = update(self.model).where(self.model.id == id).values(data)

        with Session(engine) as session:
            session.execute(statement)
            session.commit()

        return self.get_by_id(id)
    
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