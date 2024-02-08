import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.projects.models import Project
from app.tags.models import timeentry_tag_association_table, Tag

class TimeEntry(Base):
    __tablename__ = 'TimeEntries'
    id: Mapped[int] = mapped_column('TimeEntryID', primary_key=True)

    description: Mapped[str]
    start_time: Mapped[datetime.datetime] = mapped_column('StartTime')
    end_time: Mapped[datetime.datetime] = mapped_column('EndTime')

    project_id: Mapped[int] = mapped_column('ProjectID', ForeignKey("Projects.ProjectID"))
    project: Mapped["Project"] = relationship(Project, backref="time_entries")

    tags: Mapped[List[Tag]] = relationship(
        secondary=timeentry_tag_association_table, back_populates="time_entries"
    )

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'project_id': self.project_id
        }