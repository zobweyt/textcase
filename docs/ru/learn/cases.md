# Регистры

## Кастомные регистры

Подобно [`Boundary`](../reference/boundary.md/#textcase.boundary.Boundary), есть [`Case`](../reference/case.md/#textcase.case.Case), который предоставляет три компонента, необходимые для преобразования регистра. Это позволяет вам определить пользовательский случай, который ведет себя соответствующим образом в функциях [`convert`](../reference/convert.md/) и [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert):

```python
--8<-- "assets/snippets/cases/custom_convert.py"
```

И поскольку мы определили граничные условия, это означает, что [`textcase.is_case`](../reference/is_case.md/) также должен вести себя так, как ожидается:

```python
--8<-- "assets/snippets/cases/custom_is_case.py"
```

Чтобы узнать больше о создании границы с нуля, взгляните на [`textcase.case.Case`](../reference/case.md/#textcase.case.Case) класс.
