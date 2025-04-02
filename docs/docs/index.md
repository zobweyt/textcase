# textcase

[![Coveralls](https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main)](https://coveralls.io/github/zobweyt/textcase)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.python.org/pypi/textcase)
[![PyPI - Version](https://img.shields.io/pypi/v/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Types](https://img.shields.io/pypi/types/textcase)](https://pypi.python.org/pypi/textcase)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/textcase)](https://pypi.python.org/pypi/textcase)
[![AUR Version](https://img.shields.io/aur/version/python-textcase-git)](https://aur.archlinux.org/packages/python-textcase-git)

A feature-rich Python text case conversion library.

## Features

- **Text case conversion**: Convert strings between various text cases (e.g., snake_case, kebab-case, camelCase, etc.).
- **Extensible Design**: Easily extend the library with custom cases and boundaries.
- **Acronym Handling**: Properly detects and formats acronyms in strings (as in `HTTPRequest`).
- **Non-ASCII Support**: Handles non-ASCII characters seamlessly (no inferences on the input language itself is made).
- **100% Test Coverage**: Comprehensive tests ensure reliability and correctness.
- **Well-Documented**: Clean documentation with usage examples for easy understanding.
- **Performant**: Efficient implementation without the use of regular expressions.
- **Zero Dependencies**: The library has no external dependencies, making it lightweight and easy to integrate.

## Installation

<!-- termynal -->

```console
$ pip install textcase
---> 100%
Done!
```

## Usage

You can convert strings into a case using the [`convert`](./reference/convert.md/) function:

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

By default, [`convert`](./reference/convert.md/) and [`CaseConverter.convert`](./reference/converter.md/#textcase.converter.CaseConverter.convert) will split along a set of default word boundaries, that is

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

The library also supports non-ASCII characters. However, no inferences on the input language itself is made. For example, in Dutch, the digraph "ij" is treated as two separate Unicode characters and will not be capitalized. In contrast, the character "æ" will be capitalized as expected. Also, in English the text "I THINK I DO" will be converted to "i think i do", not "I think I do". This means that the library can handle various characters:

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
