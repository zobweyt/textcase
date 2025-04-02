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

You can convert strings into a case using the [`convert`](./../en/reference/convert.md/) function:

```python
--8<-- "assets/snippets/index/convert.py"
```

By default, [`convert`](./../en/reference/convert.md/) and [`CaseConverter.convert`](./reference/converter.md/#textcase.converter.CaseConverter.convert) will split along a set of default word boundaries, that is

- underscores `_`,
- hyphens `-`,
- spaces ` `,
- changes in capitalization from lowercase to uppercase `aA`,
- adjacent digits and letters `a1`, `1a`, `A1`, `1A`,
- and acroynms `AAa` (as in `HTTPRequest`).

For more precision, you can specify boundaries to split based on the word boundaries of a particular case. For example, splitting from snake case will only use underscores as word boundaries:

```python
--8<-- "assets/snippets/index/precision.py"
```

This library can detect acronyms in camel-like strings. It also ignores any leading, trailing, or duplicate delimiters:

```python
--8<-- "assets/snippets/index/acronyms.py"
```

The library also supports non-ASCII characters. However, no inferences on the input language itself is made. For example, in Dutch, the digraph "ij" is treated as two separate Unicode characters and will not be capitalized. In contrast, the character "æ" will be capitalized as expected. Also, in English the text "I THINK I DO" will be converted to "i think i do", not "I think I do". This means that the library can handle various characters:

```python
--8<-- "assets/snippets/index/non_ascii.py"
```

By default, characters followed by digits and vice-versa are considered word boundaries. In addition, any special ASCII characters (besides `_` and `-`) are ignored:

```python
--8<-- "assets/snippets/index/special.py"
```

You can also test what case a string is in:

```python
--8<-- "assets/snippets/index/is_case.py"
```
