from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String, index=True)
    member = Column(String, index=True)
    content = Column(String)
    timestamp = Column(DateTime)
