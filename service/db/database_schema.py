from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from service.db.alchemy import Base


class DbWriter(Base):
    __tablename__ = 'writer_table'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    books = relationship("DbBook")


class DbBook(Base):
    __tablename__ = 'book_table'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("writer_table.id"))
    name = Column(String)
