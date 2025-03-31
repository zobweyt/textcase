#!/usr/bin/env -S just --justfile

alias l := lint
alias f := format
alias t := test
alias c := coverage
alias b := build
alias p := publish

[group("style")]
lint:
  uv run ruff check

[group("style")]
format:
  uv run ruff format

[group("test")]
test: lint
  uv run pytest

[group("test")]
coverage: lint
  uv run pytest --cov=textcase --cov-report=term-missing

[group("build")]
build: lint
  uv build

[group("publish")]
publish: format test build
  uv publish
