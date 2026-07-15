# SQLAlchemy

Рассмотрим варианты интеграции [SQLAlchemy](https://sqlalchemy.org) с [textcase][textcase].

## Автогенерация имени таблицы

Обычно имя таблицы задаётся вручную:

```python title="base.py" linenums="1" hl_lines="5"
--8<-- "docs/.snippets/integrations/sqlalchemy/base.py"
```

Чтобы не дублировать `__tablename__` в каждой модели, можно создать базовый класс:

```python title="textcase.py" linenums="1" hl_lines="1 3 6 9-12"
--8<-- "docs/.snippets/integrations/sqlalchemy/textcase.py"
```

Если вы имеете в проекте [`Pydantic`](https://pydantic.dev), то можно обойтись без этой библиотеки и применить [`pydantic.alias_generators.to_snake`](https://pydantic.dev/docs/validation/latest/api/pydantic/config#pydantic.alias_generators.to_snake). Эта функция работает похожим образом и также обрабатывает [сокращения][textcase.ACRONYM], но весит больше.

```python title="pydantic.py" linenums="1" hl_lines="1 3-4 9-12"
--8<-- "docs/.snippets/integrations/sqlalchemy/pydantic.py"
```

Используйте этот вариант, если [`Pydantic`](https://pydantic.dev) уже присутствует в проекте и вам нужен только этот сценарий. В остальных случаях предпочтительнее [textcase][textcase] из-за меньшего размера.
