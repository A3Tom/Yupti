from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from instance.config import Config

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True
)

class Base(DeclarativeBase):
    pass