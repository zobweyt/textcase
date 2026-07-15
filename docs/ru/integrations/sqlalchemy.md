# SQLAlchemy

Рассмотрим варианты интеграции [SQLAlchemy](https://sqlalchemy.org) с [textcase][textcase].

## Автогенерация имени таблицы

Обычно имя таблицы задаётся вручную:

```python
from sqlalchemy.orm import DeclarativeBase


class User(DeclarativeBase):
    __tablename__ = "user"
```

Чтобы не дублировать `__tablename__` в каждой модели, можно создать базовый класс:

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

Если вы имеете в проекте [`Pydantic`](https://pydantic.dev), то можно обойтись без этой библиотеки и применить [`pydantic.alias_generators.to_snake`](https://pydantic.dev/docs/validation/latest/api/pydantic/config#pydantic.alias_generators.to_snake). Эта функция работает похожим образом и также обрабатывает [сокращения][textcase.ACRONYM], но весит больше.

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

Используйте этот вариант, если [`Pydantic`](https://pydantic.dev) уже присутствует в проекте и вам нужен только этот сценарий. В остальных случаях предпочтительнее [textcase][textcase] из-за меньшего размера.
