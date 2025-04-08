# Converter

## Case Converter Class

Case conversion takes place in two parts. The first splits an identifier into a series of words, and the second joins the words back together. Each of these are steps are defined using the [`CaseConverter.from_case`](../reference/converter.md#textcase.converter.CaseConverter.from_case) and [`CaseConverter.to_case`](../reference/converter.md#textcase.converter.CaseConverter.to_case) functions respectively.

[`CaseConverter`](../reference/converter.md#textcase.converter.CaseConverter) is a class that encapsulates the boundaries used for splitting and the pattern and delimiter for mutating and joining. The [`CaseConverter.convert`](../reference/converter.md#textcase.converter.CaseConverter.convert) method will apply the boundaries, pattern, and delimiter appropriately. This lets you define the parameters for case conversion upfront:

```python exec="true" source="tabbed-left" tabs="converter.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/converter/converter.py"
```

For more details on how strings are converted, see the docs for [`textcase.converter.CaseConverter`](../reference/converter.md#textcase.converter.CaseConverter).
