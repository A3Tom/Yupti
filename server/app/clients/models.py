from sqlalchemy.orm import Mapped, mapped_column
from app.common.database import Base

class Client(Base):
    __tablename__ = 'Clients'

    id: Mapped[int] = mapped_column('ClientID', primary_key=True)
    name: Mapped[str] = mapped_column()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'projects': [project.to_dict() for project in self.projects]
        }