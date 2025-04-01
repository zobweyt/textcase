import pytest

from textcase import pattern
from textcase.boundary import DEFAULT_BOUNDARIES
from textcase.case import CAMEL, SNAKE
from textcase.converter import CaseConverter


def test_case_converter_init() -> None:
    converter = CaseConverter()

    assert converter.boundaries == list(DEFAULT_BOUNDARIES)
    assert converter.pattern([""]) == [""]
    assert converter.delimiter == ""


def test_case_converter_to_case() -> None:
    converter = CaseConverter()

    assert converter.to_case(SNAKE).convert("Hello World") == "hello_world"
    assert converter.to_case(CAMEL).convert("hello world") == "helloWorld"


def test_case_converter_from_case() -> None:
    converter = CaseConverter()
    converter.from_case(SNAKE)

    assert converter.boundaries == list(SNAKE.boundaries)


def test_case_converter_chain_methods() -> None:
    converter = CaseConverter()

    assert converter.to_case(SNAKE).convert("Hello World") == "hello_world"
    assert converter.from_case(SNAKE).convert("hello_world") == "hello_world"


def test_case_converter_empty_string() -> None:
    converter = CaseConverter()

    assert converter.to_case(SNAKE).convert("") == ""


def test_case_converter_single_word() -> None:
    converter = CaseConverter()

    assert converter.to_case(SNAKE).convert("Hello") == "hello"
    assert converter.to_case(CAMEL).convert("hello") == "hello"


def test_case_converter_complex() -> None:
    converter = CaseConverter()
    converter.pattern = pattern.camel
    converter.delimiter = "_"

    assert converter.convert("My Special Case") == "my_Special_Case"

    converter.from_case(CAMEL)
    converter.to_case(SNAKE)

    assert converter.convert("mySpecialCase") == "my_special_case"


if __name__ == "__main__":
    pytest.main()
