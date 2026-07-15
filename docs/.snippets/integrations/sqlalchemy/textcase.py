from typing import Any

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase

from textcase import snake


class Base(DeclarativeBase):
    @declared_attr
    @classmethod
    def __tablename__(cls) -> Any:  # noqa: ANN401
        return snake(cls.__name__)


class User(Base): ...
