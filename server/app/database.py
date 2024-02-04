from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from instance.config import Config

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True
)