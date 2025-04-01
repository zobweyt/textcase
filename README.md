# textcase

[![Coveralls](https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main)](https://coveralls.io/github/zobweyt/textcase)
[![PyPI - Version](https://img.shields.io/pypi/v/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Types](https://img.shields.io/pypi/types/textcase)](https://pypi.python.org/pypi/textcase)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/textcase)](https://pypi.python.org/pypi/textcase)

A feature complete Python text case conversion library.

## Installation

Create and activate a virtual environment and then install `textcase`:

```sh
pip install textcase
```

## Example

You can convert strings into a case using the [`textcase.convert`](./textcase/__init__.py?plain=1#48) function:

```python
from textcase import case, convert

print(convert("ronnie james dio", case.SNAKE))     # ronnie_james_dio
print(convert("Ronnie_James_dio", case.CONSTANT))  # RONNIE_JAMES_DIO
print(convert("RONNIE_JAMES_DIO", case.KEBAB))     # ronnie-james-dio
print(convert("RONNIE-JAMES-DIO", case.CAMEL))     # ronnieJamesDio
print(convert("ronnie-james-dio", case.PASCAL))    # RonnieJamesDio
print(convert("RONNIE JAMES DIO", case.LOWER))     # ronnie james dio
print(convert("ronnie james dio", case.UPPER))     # RONNIE JAMES DIO
print(convert("ronnie-james-dio", case.TITLE))     # Ronnie James Dio
print(convert("ronnie james dio", case.SENTENCE))  # Ronnie james dio
```

By default, [`textcase.convert`](./textcase/__init__.py?plain=1#48) and [`textcase.converter.CaseConverter.convert`](./textcase/converter.py?plain=1#58) will split along a set of default word boundaries, that is

- underscores `_`,
- hyphens `-`,
- spaces ` `,
- changes in capitalization from lowercase to uppercase `aA`,
- adjacent digits and letters `a1`, `1a`, `A1`, `1A`,
- and acroynms `AAa` (as in `HTTPRequest`).

For more precision, you can specify boundaries to split based on the word boundaries of a particular case. For example, splitting from snake case will only use underscores as word boundaries:

```python
from textcase import boundary, case, convert

print(convert("2020-04-16_my_cat_cali", case.TITLE))                          # 2020 04 16 My Cat Cali
print(convert("2020-04-16_my_cat_cali", case.TITLE, (boundary.UNDERSCORE,)))  # 2020-04-16 My Cat Cali
```

This library can detect acronyms in camel-like strings. It also ignores any leading, trailing, or duplicate delimiters:

```python
from textcase import case, convert

print(convert("IOStream", case.SNAKE))             # io_stream
print(convert("myJSONParser", case.SNAKE))         # my_json_parser
print(convert("__weird--var _name-", case.SNAKE))  # weird_var_name
```

It also works non-ascii characters. However, no inferences on the language itself is made. For instance, the digraph ij in Dutch will not be capitalized, because it is represented as two distinct Unicode characters. However, æ would be capitalized:

```python
from textcase import case, convert

print(convert("GranatÄpfel", case.KEBAB))    # granat-äpfel
print(convert("ПЕРСПЕКТИВА24", case.TITLE))  # Перспектива 24
print(convert("ὈΔΥΣΣΕΎΣ", case.LOWER))       # ὀδυσσεύς
```

By default, characters followed by digits and vice-versa are considered word boundaries. In addition, any special ASCII characters (besides `_` and `-`) are ignored:

```python
from textcase import case, convert

print(convert("E5150", case.SNAKE))              # e_5150
print(convert("10,000Days", case.SNAKE))         # 10,000_days
print(convert("Hello, world!", case.UPPER))      # HELLO, WORLD!
print(convert("ONE\nTWO\nTHREE", case.TITLE))    # One\ntwo\nthree
```

You can also test what case a string is in:

```python
from textcase import case, is_case

print(is_case("css-class-name", case.KEBAB))  # True
print(is_case("css-class-name", case.SNAKE))  # False
print(is_case("UPPER_CASE_VAR", case.SNAKE))  # False
```

## Boundary Specificity

It can be difficult to determine how to split a string into words. That is why this case provides the [`textcase.convert`](./textcase/__init__.py?plain=1#48) and [`textcase.converter.CaseConverter.convert`](./textcase/converter.py?plain=1#58) functionality, but sometimes that isn’t enough to meet a specific use case.

Say an identifier has the word `2D`, such as `scale2D`. No exclusive usage of [`textcase.convert`](./textcase/__init__.py?plain=1#48) or [`textcase.converter.CaseConverter.convert`](./textcase/converter.py?plain=1#58) will be enough to solve the problem. In this case we can further specify which boundaries to split the string on. This library provides some patterns for achieving this specificity. We can specify what boundaries we want to split on using instances of the [`textcase.boundary.Boundary`](./textcase/boundary.py?plain=1#26) class:

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

To learn more about building a boundary from scratch, take a look at the [`textcase.boundary.Boundary`](./textcase/boundary.py?plain=1#26) class.

## Custom Case

Simular to [`textcase.boundary.Boundary`](./textcase/boundary.py?plain=1#26), there is [`textcase.case.Case`](./textcase/case.py?plain=1#36) that exposes the three components necessary for case conversion. This allows you to define a custom case that behaves appropriately in the [`textcase.convert`](./textcase/__init__.py?plain=1#48) and [`textcase.converter.CaseConverter.convert`](./textcase/converter.py?plain=1#58) functions:

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

And because we defined boundary conditions, this means [`textcase.is_case`](./textcase/__init__.py?plain=1#28) should also behave as expected:

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

## Case converter class

Case conversion takes place in two parts. The first splits an identifier into a series of words, and the second joins the words back together. Each of these are steps are defined using the [`textcase.converter.CaseConverter.from_case`](./textcase/converter.py?plain=1#101) and [`textcase.converter.CaseConverter.to_case`](./textcase/converter.py?plain=1#88) functions respectively.

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

For more details on how strings are converted, see the docs for [`textcase.converter.CaseConverter`](./textcase/converter.py?plain=1#27).

## API

| Modules                                         |                                                      |
| ----------------------------------------------- | ---------------------------------------------------- |
| [`textcase.boundary`](./textcase/boundary.py)   | Conditions for splitting an identifier into words.   |
| [`textcase.case`](./textcase/case.py)           | Case definitions for text transformation.            |
| [`textcase.converter`](./textcase/converter.py) | Text case conversion between different case formats. |
| [`textcase.pattern`](./textcase/pattern.py)     | Functions for transforming a list of words.          |

| Classes                                                                  |                                                                                |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| [`textcase.boundary.Boundary`](./textcase/boundary.py?plain=1#26)        | Represents a condition for splitting an identifier into words.                 |
| [`textcase.case.Case`](./textcase/case.py?plain=1#36)                    | Represents a text case format for transformation.                              |
| [`textcase.converter.CaseConverter`](./textcase/converter.py?plain=1#27) | Represents a utility class for converting text between different case formats. |

| Constants                                                                    |                                                                                                                               |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [`textcase.boundary.UNDERSCORE`](./textcase/boundary.py?plain=1#56)          | Splits on `_`, consuming the character on segmentation.                                                                       |
| [`textcase.boundary.HYPHEN`](./textcase/boundary.py?plain=1#66)              | Splits on `-`, consuming the character on segmentation.                                                                       |
| [`textcase.boundary.SPACE`](./textcase/boundary.py?plain=1#76)               | Splits on space, consuming the character on segmentation.                                                                     |
| [`textcase.boundary.LOWER_UPPER`](./textcase/boundary.py?plain=1#86)         | Splits where a lowercase letter is followed by an uppercase letter.                                                           |
| [`textcase.boundary.UPPER_LOWER`](./textcase/boundary.py?plain=1#96)         | Splits where an uppercase letter is followed by a lowercase letter. This is seldom used.                                      |
| [`textcase.boundary.ACRONYM`](./textcase/boundary.py?plain=1#107)            | Splits where two uppercase letters are followed by a lowercase letter, identifying acronyms.                                  |
| [`textcase.boundary.LOWER_DIGIT`](./textcase/boundary.py?plain=1#119)        | Splits where a lowercase letter is followed by a digit.                                                                       |
| [`textcase.boundary.UPPER_DIGIT`](./textcase/boundary.py?plain=1#129)        | Splits where an uppercase letter is followed by a digit.                                                                      |
| [`textcase.boundary.DIGIT_LOWER`](./textcase/boundary.py?plain=1#139)        | Splits where a digit is followed by a lowercase letter.                                                                       |
| [`textcase.boundary.DIGIT_UPPER`](./textcase/boundary.py?plain=1#149)        | Splits where a digit is followed by an uppercase letter.                                                                      |
| [`textcase.boundary.DEFAULT_BOUNDARIES`](./textcase/boundary.py?plain=1#159) | Default boundaries used for splitting strings into words, including underscores, hyphens, spaces, and capitalization changes. |
| [`textcase.case.SNAKE`](./textcase/case.py?plain=1#58)                       | Snake case strings are delimited by underscores `_` and are all lowercase.                                                    |
| [`textcase.case.CONSTANT`](./textcase/case.py?plain=1#65)                    | Constant case strings are delimited by underscores `_` and are all uppercase.                                                 |
| [`textcase.case.KEBAB`](./textcase/case.py?plain=1#72)                       | Kebab case strings are delimited by hyphens `-` and are all lowercase.                                                        |
| [`textcase.case.CAMEL`](./textcase/case.py?plain=1#79)                       | Camel case strings are lowercase, but for every word _except the first_ the first letter is capitalized.                      |
| [`textcase.case.PASCAL`](./textcase/case.py?plain=1#92)                      | Pascal case strings are lowercase, but for every word the first letter is capitalized.                                        |
| [`textcase.case.LOWER`](./textcase/case.py?plain=1#105)                      | Lowercase strings are delimited by spaces and all characters are lowercase.                                                   |
| [`textcase.case.UPPER`](./textcase/case.py?plain=1#112)                      | Uppercase strings are delimited by spaces and all characters are uppercase.                                                   |
| [`textcase.case.TITLE`](./textcase/case.py?plain=1#119)                      | Title case strings are delimited by spaces. Only the leading character of each word is uppercase.                             |
| [`textcase.case.SENTENCE`](./textcase/case.py?plain=1#126)                   | Sentence case strings are delimited by spaces. Only the leading character of the first word is uppercase.                     |

| Functions                                                                |                                                                         |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| [`textcase.is_case`](./textcase/__init__.py?plain=1#28)                  | Check if the given text matches the specified case format.              |
| [`textcase.convert`](./textcase/__init__.py?plain=1#48)                  | Convert the given text to the specified case format.                    |
| [`textcase.boundary.split`](./textcase/boundary.py?plain=1#182)          | Split an identifier into a list of words using the provided boundaries. |
| [`textcase.boundary.get_boundaries`](./textcase/boundary.py?plain=1#182) | Identifies boundaries present in the given text.                        |
| [`textcase.pattern.lower`](./textcase/pattern.py?plain=1#33)             | Convert all words to lowercase.                                         |
| [`textcase.pattern.upper`](./textcase/pattern.py?plain=1#49)             | Convert all words to uppercase.                                         |
| [`textcase.pattern.capital`](./textcase/pattern.py?plain=1#65)           | Capitalize the first letter of each word and make the rest lowercase.   |
| [`textcase.pattern.camel`](./textcase/pattern.py?plain=1#81)             | Convert the first word to lowercase and capitalize the remaining words. |
| [`textcase.pattern.sentence`](./textcase/pattern.py?plain=1#99)          | Capitalize the first word and make the remaining words lowercase.       |
