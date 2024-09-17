from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer ,primary_key=True)
    name = Column(String, nullable=True)
    address = Column(String, nullable=True)
    age = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=False)

Base.metadata.create_all(engine)