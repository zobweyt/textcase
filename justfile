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
  uv run --locked --group dev pre-commit install

[doc("Run style recipes on source files")]
[group("style")]
style: lint check format

[doc("Run mypy on source files")]
[group("style")]
lint:
  uv run --locked --group style mypy

[doc("Run Ruff on source files")]
[group("style")]
check:
  uv run --locked --group style ruff check --fix

[doc("Run Ruff formatter on source files")]
[group("style")]
format:
  uv run --locked --group style ruff format

[doc("Run test suite using pytest")]
[group("tests")]
test:
  uv run --locked --group tests pytest --doctest-modules

[doc("Generate test coverage report")]
[group("tests")]
coverage:
  uv run --locked --group tests pytest --doctest-modules --cov=textcase --cov-report=term-missing --cov-report=lcov:coverage.lcov

[doc("Serve documentation locally in watch mode")]
[group("docs")]
docs-serve:
  uv run --locked --group docs --group style mkdocs serve -f mkdocs.yaml

[doc("Build documentation static files locally")]
[group("docs")]
docs-build: docs-changelog
  uv run --locked --group docs --group style mkdocs build -f mkdocs.yaml

[doc("Deploy documentation to GitHub Pages")]
[group("docs")]
[private]
docs-gh-deploy: docs-changelog
  uv run --locked --group docs --group style mkdocs gh-deploy --force -f mkdocs.yaml

[doc("Build documentation static files locally")]
[group("changelog")]
docs-changelog:
  uv run --locked --group docs git cliff -o CHANGELOG.md

[doc("Build package into source distributions and wheels")]
[group("build")]
build:
  uv build

[doc("Build and upload distributions to PyPI")]
[group("publish")]
[confirm("Do you really want to build and upload distributions to PyPI (y/N)?")]
publish: style test build
  uv publish

[unix]
[doc("Clean build artifacts and cache directories")]
[group("clean")]
[confirm("Do you really want to clean build artifacts and cache directories (y/N)?")]
clean:
  find . -type d -name __pycache__ -exec rm -rf {} +
  rm -rf .cache .mypy_cache .pytest_cache .ruff_cache .venv *.egg-info .coverage build dist site coverage.lcov
