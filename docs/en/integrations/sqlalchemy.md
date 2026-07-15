# SQLAlchemy

Let's explore the integration options of [SQLAlchemy](https://sqlalchemy.org) with [textcase][textcase].

## Table Name Autogeneration

Typically, table names are specified manually:

```python title="base.py" linenums="1" hl_lines="5"
--8<-- "docs/.snippets/integrations/sqlalchemy/base.py"
```

To avoid duplicating `__tablename__` in every model, you can create a base class:

```python title="textcase.py" linenums="1" hl_lines="1 3 6 9-13"
--8<-- "docs/.snippets/integrations/sqlalchemy/textcase.py"
```

If you have [`Pydantic`](https://pydantic.dev) in your project, you can achieve this without the extra library by using [`pydantic.alias_generators.to_snake`](https://pydantic.dev/docs/validation/latest/api/pydantic/config#pydantic.alias_generators.to_snake). This function works similarly and also handles [acronyms][textcase.ACRONYM], but it has a larger footprint.

```python title="pydantic.py" linenums="1" hl_lines="1 3-4 8-12"
--8<-- "docs/.snippets/integrations/sqlalchemy/pydantic.py"
```

Use this option if [`Pydantic`](https://pydantic.dev) is already present in your project and you only need this specific feature. In all other cases, [textcase][textcase] is preferable due to its smaller footprint.
