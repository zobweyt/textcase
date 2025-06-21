---
hide:
  - footer
---

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
  Python library for text case conversions.
</p>

<p align="center">
  <a href="https://coveralls.io/github/zobweyt/textcase" target="_blank">
    <img src="https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main" alt="Coveralls"/>
  </a>
  <a href="https://pypistats.org/packages/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/dm/textcase" alt="PyPI - Downloads"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/v/textcase.svg" alt="PyPI - Version"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/textcase.svg" alt="PyPI - Python Version"/>
  </a>
</p>

## Features

<div class="md-emoji-list" markdown>

- :fire: <span>**Text case conversion**: [convert](#usage) strings between various text cases (e.g., [snake_case][textcase.snake], [kebab-case][textcase.kebab], [camelCase][textcase.camel], etc.).</span>
- :fire: <span>**Extensible**: extend the library with custom word [boundaries](./learn/boundaries.md) and [cases](./learn/cases.md).</span>
- :fire: <span>**Accurate**: [handles any word boundaries](#precision) in strings including [acronyms][textcase.ACRONYM] (as in `#!py "HTTPRequest"`).</span>
- :fire: <span>**Non-ASCII Support**: handles [non-ASCII characters](#non-ascii-characters) seamlessly (no inferences on the input language itself is made).</span>
- :fire: <span>**Tiny, Performant & Zero Dependencies**: a regex-free, efficient library that stays lightweight with no external dependencies.</span>
- :fire: <span>**100% <abbr title="The amount of code that is automatically tested">test coverage</abbr>**: every line of code is rigorously tested for reliability.</span>
- :fire: <span>**100% <abbr title="Python type annotations, with this your editor and external tools can give you better support">type annotated</abbr> codebase**: full type annotations for best developer experience.</span>

</div>

## Installation

<!-- termynal -->

```console
$ pip install textcase
---> 100%
Done!
```

## Usage

Convert a string to a text case:

```py title="cases.py" linenums="1"
--8<-- "docs/.snippets/cases.py"
```

You can also test what case a string is in:

```py title="match.py" linenums="1" hl_lines="3-5"
--8<-- "docs/.snippets/match.py"
```

### Boundaries

By default, the library will words split along a set of default word boundaries, that is:

- Underscores: `#!py "_"`,
- Hyphens: `#!py "-"`,
- Spaces: `#!py " "`,
- Interpuncts: `#!py "·"`,
- Changes in capitalization from lowercase to uppercase: `#!py "aA"`,
- Adjacent digits and letters: `#!py "a1"`, `#!py "1a"`, `#!py "A1"`, `#!py "1A"`,
- Acronyms: `#!py "AAa"` (as in `#!py "HTTPRequest"`).

You can learn more about boundaries [here](./learn/boundaries.md).

### Precision

For more precision, you can specify boundaries to split based on the word boundaries of a particular case.
For example, you can explicitly specify which boundaries will be used:

```py title="precision.py" linenums="1" hl_lines="4"
--8<-- "docs/.snippets/precision.py"
```

This library can detect acronyms in camel-like strings. It also ignores any leading, trailing, or duplicate delimiters:

```py title="acronyms.py" linenums="1" hl_lines="3-5"
--8<-- "docs/.snippets/acronyms.py"
```

### Non-ASCII Characters

The library also supports non-ASCII characters. **However, no inferences on the input language itself is made**.
For example, in Dutch, the digraph `#!py "ij"` is treated as two separate Unicode characters and will not be capitalized.
In contrast, the character `#!py "æ"` will be capitalized as expected.
Also, in English the text `#!py "I THINK I DO"` will be converted to `#!py "i think i do"`, not `#!py "I think I do"`.
This means that the library can handle various characters:

```py title="non_ascii.py" linenums="1" hl_lines="3-5"
--8<-- "docs/.snippets/non_ascii.py"
```

### Punctuation

By default [punctuation][string.punctuation] characters are stripped
(excluding the [`delimiter`][textcase.Case.delimiter] of the current text case)
and other special characters are ignored.
You can control this behavior using the `strip_punctuation` argument:

```py title="punctuation.py" linenums="1" hl_lines="7-8"
--8<-- "docs/.snippets/punctuation.py"
```
