from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, relationship, Column, Integer, String, DateTime, Boolean
from dateutil import parser
import datetime

Base = declarative_base()

group_categories = Table('group_categories', Base.metadata,
        Column('group_id', Integer, ForeignKey('groups.id')),
        Column('category_id', Integer, ForeignKey('categories.id'))
)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True)
    name = Column(String(255))
    is_active = Column(Boolean)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key = True)
    name = Column(String(255))
    is_active = Column(Boolean)
    
    categories = relationship('Category', secondary=group_categories, backref='groups')


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Group('%s')>" % (self.name)

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
