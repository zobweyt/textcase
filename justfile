#!/usr/bin/env -S just --justfile

alias s := style
alias l := lint
alias c := check
alias f := format
alias t := test
alias v := coverage
alias d := docs-serve
alias b := build
alias p := publish

[doc("List available recipes")]
[private]
default:
  @just --list --unsorted

[doc("Initialize development environment")]
init:
  @uv sync --group dev > /dev/null 2>&1
  uv run pre-commit install

[doc("Run style recipes on source files")]
[group("style")]
style: lint check format

[doc("Run mypy on source files")]
[group("style")]
lint:
  @uv sync --group style > /dev/null 2>&1
  uv run mypy

[doc("Run Ruff on source files")]
[group("style")]
check:
  @uv sync --group style > /dev/null 2>&1
  uv run ruff check --fix

[doc("Run Ruff formatter on source files")]
[group("style")]
format:
  @uv sync --group style > /dev/null 2>&1
  uv run ruff format

[doc("Run test suite using pytest")]
[group("tests")]
test:
  @uv sync --group tests > /dev/null 2>&1
  uv run pytest --doctest-modules

[doc("Generate test coverage report")]
[group("tests")]
coverage:
  @uv sync --group tests > /dev/null 2>&1
  uv run pytest --doctest-modules --cov=textcase --cov-report=term-missing --cov-report=lcov:coverage.lcov

[doc("Serve documentation locally in watch mode")]
[group("docs")]
docs-serve:
  @uv sync --group docs --group style > /dev/null 2>&1
  uv run mkdocs serve -f mkdocs.yaml

[doc("Build documentation static files locally")]
[group("docs")]
docs-build:
  @uv sync --group docs --group style > /dev/null 2>&1
  uv run mkdocs build -f mkdocs.yaml

[doc("Deploy documentation to GitHub Pages")]
[group("docs")]
[private]
docs-gh-deploy:
  @uv sync --group docs --group style > /dev/null 2>&1
  uv run mkdocs gh-deploy --force -f mkdocs.yaml

[doc("Build package into source distributions and wheels")]
[group("build")]
build:
  @uv sync > /dev/null 2>&1
  uv build

[doc("Build and upload distributions to PyPI")]
[group("publish")]
[confirm("Do you really want to build and upload distributions to PyPI (y/N)?")]
publish: style test build
  @uv sync > /dev/null 2>&1
  uv publish

[unix]
[doc("Clean build artifacts and cache directories")]
[group("clean")]
[confirm("Do you really want to clean build artifacts and cache directories (y/N)?")]
clean:
  find . -type d -name __pycache__ -exec rm -rf {} +
  rm -rf .cache .mypy_cache .pytest_cache .ruff_cache .venv *.egg-info .coverage build dist site coverage.lcov
