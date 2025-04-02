# Cases

## Custom Case

Simular to [`Boundary`](../reference/boundary.md/#textcase.boundary.Boundary), there is [`Case`](../reference/case.md/#textcase.case.Case) that exposes the three components necessary for case conversion. This allows you to define a custom case that behaves appropriately in the [`convert`](../reference/convert.md/) and [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) functions:

```python
--8<-- "assets/snippets/cases/custom_convert.py"
```

And because we defined boundary conditions, this means [`textcase.is_case`](../reference/is_case.md/) should also behave as expected:

```python
--8<-- "assets/snippets/cases/custom_is_case.py"
```

To learn more about building a boundary from scratch, take a look at the [`textcase.case.Case`](../reference/case.md/#textcase.case.Case) class.
