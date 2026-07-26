# Contributing

We welcome all contributions! Please follow this guide to set up your environment and submit your changes.

## Quick Start

[Fork](https://github.com/zobweyt/textcase/fork) this repository and clone it locally.

Before introducing massive features, please [open an issue](https://github.com/zobweyt/textcase/issues/new?template=feature_request.yaml) first to discuss it.

## Development

We use [`uv`](https://github.com/astral-sh/uv) as the project manager. After cloning, set up git hooks:

```sh
uv run task prepare
```

Then verify your setup:

```sh
uv run task test
```

Python 3.9+ is needed for this project. Use any version in this range; if a test fails on a specific version, try another.

### Guidelines

- Update tests (including doctests) and documentation after adding code.
- Commit using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and open a pull request to `main`.
- To extend the library with custom boundaries or cases, see the [advanced documentation](https://zobweyt.github.io/textcase/advanced/cases/).

### Commands

- Run all code quality checks (linting, type checking, and formatting):

  ```sh
  uv run task style
  ```

- Run type checking with [`ty`](https://github.com/astral-sh/ty):

  ```sh
  uv run task lint
  ```

- Run linting and auto-fix issues with [`ruff`](https://github.com/astral-sh/ruff):

  ```sh
  uv run task check
  ```

- Format code with [`ruff`](https://github.com/astral-sh/ruff):

  ```sh
  uv run task format
  ```

- Run the test suite:

  ```sh
  uv run task test
  ```

- Run the test suite with coverage reporting:

  ```sh
  uv run task coverage
  ```

- Serve the documentation locally:

  ```sh
  uv run task serve
  ```

## Documentation

We welcome contributions to the documentation: updating outdated content, adding missing sections, and correcting typos. Please add documentation in English first — translations into other languages are welcome but not required.

| Code | Name    | Progress | Maintainers                            |
| :--- | :------ | :------- | :------------------------------------- |
| `en` | English | 100%     | [@zobweyt](https://github.com/zobweyt) |
| `ru` | Russian | 100%     | [@zobweyt](https://github.com/zobweyt) |
