## Case Converter Class

Case conversion takes place in two parts. The first splits an identifier into a series of words, and the second joins the words back together. Each of these are steps are defined using the [`textcase.converter.CaseConverter.from_case`](../reference/converter.md#textcase.converter.CaseConverter.from_case) and [`textcase.converter.CaseConverter.to_case`](../reference/converter.md#textcase.converter.CaseConverter.to_case) functions respectively.

`CaseConverter` is a class that encapsulates the boundaries used for splitting and the pattern and delimiter for mutating and joining. The convert method will apply the boundaries, pattern, and delimiter appropriately. This lets you define the parameters for case conversion upfront:

```python
from textcase import CaseConverter, case, pattern

converter = CaseConverter()
converter.pattern = pattern.camel
converter.delimiter = "_"

print(converter.convert("My Special Case"))  # my_Special_Case

converter.from_case(case.CAMEL)
converter.to_case(case.SNAKE)

print(converter.convert("mySpecialCase"))  # my_special_case
```

For more details on how strings are converted, see the docs for [`textcase.converter.CaseConverter`](../reference/converter.md#textcase.converter.CaseConverter).
