import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.common.database import Base
from app.clients.models import Client

class Project(Base):
    __tablename__ = 'Projects'
    id: Mapped[int] = mapped_column('ProjectID', primary_key=True)

    name: Mapped[str]
    description: Mapped[str]
    start_date: Mapped[datetime.datetime] = mapped_column("StartDate")
    end_date: Mapped[datetime.datetime] = mapped_column("EndDate")

    client_id: Mapped[int] = mapped_column('ClientID', ForeignKey("Clients.ClientID"))
    client: Mapped["Client"] = relationship(Client, backref="projects")

    def to_dict(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date
        }