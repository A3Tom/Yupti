from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.time_entries.models import TimeEntry

class Tag(Base):
    __tablename__ = 'Tags'
    id: Mapped[int] = mapped_column('TagID', primary_key=True)
    name: Mapped[str] = mapped_column()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

# Ahhh I know this isn't how you do this really and it probably won't work - will get working later
class TimeEntryTag(Base):
    __tablename__ = 'TimeEntryTags'
    tag_id: Mapped[int] = mapped_column('TagID', ForeignKey("Tags.TagID"))
    tag = relationship(Tag, backref="Tag")
    
    time_entry_id: Mapped[int] = mapped_column('TimeEntryID', ForeignKey("TimeEntries.TimeEntryID"))
    time_entry = relationship(TimeEntry, backref="time_entries")