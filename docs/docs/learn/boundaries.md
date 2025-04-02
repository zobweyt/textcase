
## Boundary Specificity

It can be difficult to determine how to split a string into words. That is why this case provides the [`convert`](../reference/convert.md/) and [`textcase.converter.CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) functionality, but sometimes that isn’t enough to meet a specific use case.

Say an identifier has the word `2D`, such as `scale2D`. No exclusive usage of [`textcase.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) or [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) will be enough to solve the problem. In this case we can further specify which boundaries to split the string on. This library provides some patterns for achieving this specificity. We can specify what boundaries we want to split on using instances of the [`Boundary`](../reference/boundary.md/#textcase.boundary.Boundary) class:

```python
from textcase import boundary, case, convert

# Not quite what we want
print(convert("scale2D", case.SNAKE, case.CAMEL.boundaries))    # scale_2_d

# Write boundaries explicitly
print(convert("scale2D", case.SNAKE, (boundary.LOWER_DIGIT,)))  # scale_2d
```

## Custom Boundaries

This library provides a number of constants for boundaries associated with common cases. But you can create your own boundary to split on other criteria:

```python
from textcase import case, convert
from textcase.boundary import Boundary

# Not quite what we want
print(convert("coolers.revenge", case.TITLE))  # Coolers.revenge

# Define custom boundary
DOT = Boundary(
    satisfies=lambda text: text.startswith("."),
    length=1,
)

print(convert("coolers.revenge", case.TITLE, (DOT,)))  # Coolers Revenge

# Define complex custom boundary
AT_LETTER = Boundary(
    satisfies=lambda text: (len(text) > 1 and text[0] == "@") and (text[1] == text[1].lower()),
    start=1,
    length=0,
)

print(convert("name@domain", case.TITLE, (AT_LETTER,)))  # Name@ Domain
```

To learn more about building a boundary from scratch, take a look at the [`textcase.boundary.Boundary`](../reference/boundary.md/#textcase.boundary.Boundary) class.
