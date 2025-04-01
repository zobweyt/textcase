from textcase import pattern


def test_lower() -> None:
    assert tuple(pattern.lower(("Hello", "World"))) == ("hello", "world")


def test_upper() -> None:
    assert tuple(pattern.upper(("Hello", "World"))) == ("HELLO", "WORLD")


def test_capital() -> None:
    assert tuple(pattern.capital(("hello", "world"))) == ("Hello", "World")


def test_camel() -> None:
    assert tuple(pattern.camel(("hello", "world"))) == ("hello", "World")


def test_sentence() -> None:
    assert tuple(pattern.sentence(("hello", "world"))) == ("Hello", "world")
