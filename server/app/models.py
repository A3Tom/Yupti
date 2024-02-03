import datetime
from typing import List
from run import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = 'Clients'

    id: Mapped[int] = mapped_column('ClientID', primary_key=True)
    name: Mapped[str]

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'projects': [project.to_dict() for project in self.projects]
        }

class Project(Base):
    __tablename__ = 'Projects'
    project_id: Mapped[int] = mapped_column('ProjectID', primary_key=True)

    name: Mapped[str]
    description: Mapped[str]
    start_date: Mapped[datetime.datetime] = mapped_column("StartDate")
    end_date: Mapped[datetime.datetime] = mapped_column("EndDate")

    client_id: Mapped[int] = mapped_column('ClientID', ForeignKey("Clients.ClientID"))
    client: Mapped["Client"] = relationship(Client, backref="projects")

    def to_dict(self):
        return {
            'id': self.project_id,
            'client_id': self.client_id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date
        }

class TimeEntry(Base):
    __tablename__ = 'TimeEntries'
    time_entry_id = db.Column('TimeEntryID', db.Integer, primary_key=True)
    # project_id = db.Column(db.Integer, db.ForeignKey('ProjectID'), nullable=False)
    start_time = db.Column('StartDate', db.DateTime, nullable=False)
    end_time = db.Column('EndDate', db.DateTime, nullable=False)
    description = db.Column(db.String(1023))

    # project_id: Mapped[int] = mapped_column('ProjectID', ForeignKey("Project.ProjectID"))

class Tag(Base):
    __tablename__ = 'Tags'
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    # time_entries = db.relationship('TimeEntry', secondary='time_entry_tags', backref='tags')

class TimeEntryTag(Base):
    __tablename__ = 'TimeEntryTags'
    time_entry_id = db.Column(db.Integer, db.ForeignKey('TimeEntries.TimeEntryID'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('Tags.id'), primary_key=True)