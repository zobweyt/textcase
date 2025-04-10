# Регистры

## Кастомные регистры

Подобно [`Boundary`](../reference/boundary.md/#textcase.boundary.Boundary), есть [`Case`](../reference/case.md/#textcase.case.Case), который предоставляет три компонента, необходимые для преобразования регистра. Это позволяет вам определить пользовательский случай, который ведет себя соответствующим образом в функциях [`convert`](../reference/convert.md/) и других функциях:

```python exec="true" source="tabbed-left" tabs="custom_convert.py|output.txt" result="txt" hl_lines="13-17"
--8<-- "docs/.snippets/cases/custom_convert.py"
```

И поскольку мы определили граничные условия, это означает, что [`textcase.is_case`](../reference/is_case.md/) также должен вести себя так, как ожидается:

```python exec="true" source="tabbed-left" tabs="custom_is_case.py|output.txt" result="txt" hl_lines="19-21"
--8<-- "docs/.snippets/cases/custom_is_case.py"
```

Чтобы узнать больше о создании кастомного регистра с нуля, взгляните на класс [`textcase.case.Case`](../reference/case.md/#textcase.case.Case).
