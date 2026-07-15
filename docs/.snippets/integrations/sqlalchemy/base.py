from sqlalchemy.orm import DeclarativeBase


class User(DeclarativeBase):
    __tablename__ = "user"
