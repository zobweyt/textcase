#!/usr/bin/env -S just --justfile

alias l := lint
alias c := check
alias f := format
alias t := test
alias v := coverage
alias b := build
alias p := publish

[group("style")]
lint:
  uv run mypy

[group("style")]
check:
  uv run ruff check

[group("style")]
format:
  uv run ruff format

[group("test")]
test: check
  uv run pytest

[group("test")]
coverage: check
  uv run pytest --cov=textcase --cov-report=term-missing

[group("build")]
build: lint check
  uv build

[group("publish")]
publish: format test build
  uv publish
