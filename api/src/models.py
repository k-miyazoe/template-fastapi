from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel
from db import Base
from db import ENGINE


class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String(30), index=True)
    tag = Column(String(30), index=True)


class WordModel(BaseModel):
    word: str
    tag: str


class TestUserTable(Base):
    __tablename__ = 'test_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(128), nullable=False)


class TestUser(BaseModel):
    id: int
    name: str
    email: str


def main():
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
