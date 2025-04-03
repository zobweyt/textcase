# Boundaries

## Boundary Specificity

It can be difficult to determine how to split a string into words. That is why this case provides the [`convert`](../reference/convert.md/) and [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) functionality, but sometimes that isn’t enough to meet a specific use case.

Say an identifier has the word `2D`, such as `scale2D`. No exclusive usage of [`convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) or [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) will be enough to solve the problem. In this case we can further specify which boundaries to split the string on. This library provides some patterns for achieving this specificity. We can specify what boundaries we want to split on using instances of the [`Boundary`](../reference/boundary.md/#textcase.boundary.Boundary) class:

```python exec="true" source="tabbed-left" tabs="specificity.py|output.txt" result="txt" hl_lines="7"
--8<-- "docs/assets/snippets/boundaries/specificity.py"
```

## Custom Boundaries

This library provides a number of constants for boundaries associated with common cases. But you can create your own boundary to split on other criteria:

```python exec="true" source="tabbed-left" tabs="custom.py|output.txt" result="txt" hl_lines="8-11 16-20"
--8<-- "docs/assets/snippets/boundaries/custom.py"
```

To learn more about building a boundary from scratch, take a look at the [`textcase.boundary.Boundary`](../reference/boundary.md/#textcase.boundary.Boundary) class.
