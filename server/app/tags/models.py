from typing import List
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

timeentry_tag_association_table = Table(
    "TimeEntryTags",
    Base.metadata,
    Column("TagID", ForeignKey("Tags.TagID"), primary_key=True),
    Column("TimeEntryID", ForeignKey("TimeEntries.TimeEntryID"), primary_key=True),
)

class Tag(Base):
    __tablename__ = 'Tags'
    id: Mapped[int] = mapped_column('TagID', primary_key=True)
    name: Mapped[str] = mapped_column()
    time_entries: Mapped[List["TimeEntry"]] = relationship(
        secondary=timeentry_tag_association_table, back_populates="tags"
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
