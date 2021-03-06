from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)


from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    body = Column(String)
    author = Column(String)
    date = Column(DateTime)
