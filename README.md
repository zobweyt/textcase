<p align="center">
  <a href="https://pypi.python.org/pypi/textcase">
    <img src="https://raw.githubusercontent.com/zobweyt/textcase/refs/heads/main/docs/assets/favicon.svg" alt="textcase logo" width="96" height="96" />
  </a>
</p>

<h1 align="center">
  textcase
</h1>

<p align="center">
  A feature-rich Python text case conversion library.
</p>

<p align="center">
  <a href="https://coveralls.io/github/zobweyt/textcase" target="_blank">
    <img src="https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main" alt="Coveralls"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/badge/dependencies-0-brightgreen" alt="Dependencies"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/v/textcase.svg" alt="PyPI - Version"/>
  </a>
  <a href="https://pypistats.org/packages/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/dm/textcase" alt="PyPI - Downloads"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/textcase.svg" alt="PyPI - Python Version"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/types/textcase" alt="PyPI - Types"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/wheel/textcase" alt="PyPI - Wheel"/>
  </a>
  <a href="https://aur.archlinux.org/packages/python-textcase-git" target="_blank">
    <img src="https://img.shields.io/aur/version/python-textcase-git" alt="AUR Version"/>
  </a>
</p>

**Documentation**: https://zobweyt.github.io/textcase

**PyPI**: https://pypi.org/project/textcase

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

Create and activate a virtual environment and then install [`textcase`](https://pypi.org/projects/textcase):

```sh
pip install textcase
```

## Usage

You can convert strings into a case using the [`convert`](https://zobweyt.github.io/textcase/reference/textcase/#textcase.convert) function:

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

See [documentation](https://zobweyt.github.io/textcase) for more usage examples.
