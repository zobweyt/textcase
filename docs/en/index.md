<p align="center">
  <span>&emsp;</span>
  <span>&emsp;</span>
  <span>&emsp;</span>
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

```python id="convert" exec="true" source="tabbed-left" tabs="convert.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/convert.py"
```

By default, [`convert`](./reference/convert.md/) and [`CaseConverter.convert`](./reference/converter.md/#textcase.converter.CaseConverter.convert) will split along a set of [default word boundaries](./reference/boundary.md/#textcase.boundary.DEFAULT_BOUNDARIES), that is:

- Underscores: `_`,
- Hyphens: `-`,
- Spaces: ` `,
- Changes in capitalization from lowercase to uppercase: `aA`,
- Adjacent digits and letters: `a1`, `1a`, `A1`, `1A`,
- Acroynms: `AAa` (as in `HTTPRequest`).

For more precision, you can specify boundaries to split based on the word boundaries of a particular case. For example, you can explicitly specify which boundaries will be used:

```python id="precision" exec="true" source="tabbed-left" tabs="precision.py|output.txt" result="txt" hl_lines="4"
--8<-- "docs/assets/snippets/index/precision.py"
```

This library can detect acronyms in camel-like strings. It also ignores any leading, trailing, or duplicate delimiters:

```python id="acronyms" exec="true" source="tabbed-left" tabs="acronyms.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/acronyms.py"
```

The library also supports non-ASCII characters. **However, no inferences on the input language itself is made**. For example, in Dutch, the digraph "ij" is treated as two separate Unicode characters and will not be capitalized. In contrast, the character "æ" will be capitalized as expected. Also, in English the text "I THINK I DO" will be converted to "i think i do", not "I think I do". This means that the library can handle various characters:

```python id="non_ascii" exec="true" source="tabbed-left" tabs="non_ascii.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/non_ascii.py"
```

By default, characters followed by digits and vice-versa are considered word boundaries. In addition, any special ASCII characters (besides `_` and `-`) are ignored:

```python id="special" exec="true" source="tabbed-left" tabs="special.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/special.py"
```

You can also test what case a string is in:

```python id="is_case" exec="true" source="tabbed-left" tabs="is_case.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/is_case.py"
```
