from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from dateutil import parser
import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    message_id = Column(String(255))
    author = Column(String(255))
    xref = Column(String(255))
    bytes = Column(Integer)
    subject = Column(String(255))
    date = Column(DateTime)

    def __init__(self, message_id, author, xref, bytes, subject, date):
        self.message_id = message_id
        self.author = author
        self.xref = xref
        self.bytes = bytes
        self.subject = subject
        self.date = parser.parse(date)

    def __repr__(self):
        return "<Article('%s','%s')>" % (self.message_id, self.subject)

