# Cases

## Custom Case

Simular to [`Boundary`][textcase.boundary.Boundary], there is [`Case`][textcase.case.Case] that exposes the three components necessary for case conversion. This allows you to define a custom case that behaves appropriately in the [`convert`][textcase.convert] and other functions:

```python exec="true" source="tabbed-left" tabs="custom_convert.py|output.txt" result="txt" hl_lines="13-17"
--8<-- "docs/.snippets/cases/custom_convert.py"
```

And because we defined boundary conditions, this means [`textcase.is_case`][textcase.is_case] should also behave as expected:

```python exec="true" source="tabbed-left" tabs="custom_is_case.py|output.txt" result="txt" hl_lines="19-21"
--8<-- "docs/.snippets/cases/custom_is_case.py"
```

To learn more about building a custom case from scratch, take a look at the [textcase.case.Case][] class.
