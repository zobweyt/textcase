# SQLAlchemy

Let's explore the integration options of [SQLAlchemy](https://sqlalchemy.org) with [textcase][textcase].

## Table Name Autogeneration

Typically, table names are specified manually:

```python
from sqlalchemy.orm import DeclarativeBase


class User(DeclarativeBase):
    __tablename__ = "user"
```

To avoid duplicating `__tablename__` in every model, you can create a base class:

```python
from typing import Any

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
from textcase import snake


class Base(DeclarativeBase):
    @declared_attr
    @classmethod
    def __tablename__(cls) -> Any:
        return snake(cls.__name__)
```

If you have [`Pydantic`](https://pydantic.dev) in your project, you can achieve this without the extra library by using [`pydantic.alias_generators.to_snake`](https://pydantic.dev/docs/validation/latest/api/pydantic/config#pydantic.alias_generators.to_snake). This function works similarly and also handles [acronyms][textcase.ACRONYM], but it has a larger footprint.

```python
from typing import Any

from pydantic.alias_generators import to_snake
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    @declared_attr
    @classmethod
    def __tablename__(cls) -> Any:
        return to_snake(cls.__name__)
```

Use this option if [`Pydantic`](https://pydantic.dev) is already present in your project and you only need this specific feature. In all other cases, [textcase][textcase] is preferable due to its smaller footprint.
