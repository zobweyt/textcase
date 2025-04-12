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
  uv sync --dev
  uv run pre-commit install

[doc("Run style recipes on source files")]
[group("style")]
style: lint check format

[doc("Run mypy on source files")]
[group("style")]
lint:
  uv run mypy

[doc("Run Ruff on source files")]
[group("style")]
check:
  uv run ruff check --fix

[doc("Run Ruff formatter on source files")]
[group("style")]
format:
  uv run ruff format

[doc("Run test suite using pytest")]
[group("test")]
test:
  uv run pytest

[doc("Generate test coverage report")]
[group("test")]
coverage:
  uv run pytest --cov=textcase --cov-report=term-missing --cov-report=lcov:coverage.lcov

[unix]
[doc("Serve documentation locally in watch mode")]
[group("docs")]
docs-serve:
  PYTHONPATH=$(pwd) uv run mkdocs serve -f mkdocs.yaml

[unix]
[doc("Build documentation static files locally")]
[group("docs")]
docs-build:
  PYTHONPATH=$(pwd) uv run mkdocs build -f mkdocs.yaml

[unix]
[doc("Deploy documentation to GitHub Pages")]
[group("docs")]
[private]
docs-gh-deploy:
  PYTHONPATH=$(pwd) uv run mkdocs gh-deploy --force -f mkdocs.yaml

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
  rm -rf .cache .mypy_cache .pytest_cache .ruff_cache .coverage dist site coverage.lcov
