## Custom Case

Simular to [`textcase.boundary.Boundary`](../reference/boundary.md/#textcase.boundary.Boundary), there is [`textcase.case.Case`](../reference/case.md/#textcase.case.Case) that exposes the three components necessary for case conversion. This allows you to define a custom case that behaves appropriately in the [`convert`](../reference/convert.md/) and [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) functions:

```python
from textcase import convert
from textcase.boundary import Boundary
from textcase.case import Case
from textcase.pattern import lower

# Define custom boundary
DOT = Boundary(
    satisfies=lambda text: text.startswith("."),
    length=1,
)

# Define custom case
DOT_CASE = Case(
    boundaries=(DOT,),
    pattern=lower,
    delimiter=".",
)

print(convert("Dot case var", DOT_CASE))  # dot.case.var
```

And because we defined boundary conditions, this means [`textcase.is_case`](../reference/is_case.md/) should also behave as expected:

```python
from textcase import is_case
from textcase.boundary import Boundary
from textcase.case import Case
from textcase.pattern import lower

# Define custom boundary
DOT = Boundary(
    satisfies=lambda text: text.startswith("."),
    length=1,
)

# Define custom case
DOT_CASE = Case(
    boundaries=(DOT,),
    pattern=lower,
    delimiter=".",
)

print(is_case("dot.case.var", DOT_CASE))  # True
print(is_case("Dot case var", DOT_CASE))  # False
```
