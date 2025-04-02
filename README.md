# textcase

[![Coveralls](https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main)](https://coveralls.io/github/zobweyt/textcase)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.python.org/pypi/textcase)
[![PyPI - Version](https://img.shields.io/pypi/v/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Types](https://img.shields.io/pypi/types/textcase)](https://pypi.python.org/pypi/textcase)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/textcase)](https://pypi.python.org/pypi/textcase)
[![AUR Version](https://img.shields.io/aur/version/python-textcase-git)](https://aur.archlinux.org/packages/python-textcase-git)

A feature-rich Python text case conversion library.

**Documentation**: https://zobweyt.github.io/textcase

**PyPi**: https://pypi.org/projects/textcase

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

Create and activate a virtual environment and then install `textcase`:

```sh
pip install textcase
```

## Usage

You can convert strings into a case using the `convert` function:

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
