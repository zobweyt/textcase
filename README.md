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
    <img src="https://img.shields.io/pypi/v/textcase.svg" alt="PyPI - Version"/>
  </a>
  <a href="https://pypistats.org/packages/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/dm/textcase" alt="PyPI - Downloads"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/textcase.svg" alt="PyPI - Python Version"/>
  </a>
</p>

**Documentation**: https://zobweyt.github.io/textcase

**PyPI**: https://pypi.org/project/textcase

## Features

- **Text case conversion**: [convert](https://zobweyt.github.io/textcase/#usage) strings between various text cases (e.g., [snake_case](https://zobweyt.github.io/textcase/reference/#textcase.snake), [kebab-case](https://zobweyt.github.io/textcase/reference/#textcase.kebab), [camelCase](https://zobweyt.github.io/textcase/reference/#textcase.camel), etc.).
- **Extensible**: extend the library with custom word [boundaries](./learn/boundaries.md) and [cases](./learn/cases.md).
- **Accurate**: finds any word [boundaries](https://zobweyt.github.io/textcase/#precision) in strings including [acronyms](https://zobweyt.github.io/textcase/reference/#textcase.ACRONYM) (as in `"HTTPRequest"`).
- **Non-ASCII Support**: handles [non-ASCII characters](https://zobweyt.github.io/textcase/#non-ascii-characters) seamlessly (no inferences on the input language itself is made).
- **Tiny, Performant & Zero Dependencies**: a regex-free, efficient library that stays lightweight with no external dependencies.
- **100% <abbr title="The amount of code that is automatically tested">test coverage</abbr>**: every line of code is rigorously tested for reliability.
- **100% <abbr title="Python type annotations, with this your editor and external tools can give you better support">type annotated</abbr> codebase**: full type annotations for best developer experience.

## Installation

Create and activate a virtual environment and then install [`textcase`](https://pypi.org/projects/textcase):

```sh
pip install textcase
```

## Usage

You can convert strings into a case using the [`convert`](https://zobweyt.github.io/textcase/reference/textcase/#textcase.convert) function:

```python
import textcase

textcase.snake("Hello, world!")  # hello_world
textcase.constant("Hello, world!")  # HELLO_WORLD
textcase.kebab("Hello, world!")  # hello-world
textcase.middot("Hello, world!")  # hello·world
textcase.camel("Hello, world!")  # helloWorld
textcase.pascal("Hello, world!")  # HelloWorld
textcase.lower("Hello, world!")  # hello world
textcase.upper("Hello, world!")  # HELLO WORLD
textcase.title("Hello, world!")  # Hello World
textcase.sentence("Hello, world!")  # Hello world
```

See [documentation](https://zobweyt.github.io/textcase) for more usage examples.
