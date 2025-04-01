from textcase import case, convert


def test_e_5150() -> None:
    assert convert("E5150", case.SNAKE) == "e_5150"


def test_10_000_days() -> None:
    assert convert("10,000Days", case.SNAKE) == "10,000_days"


def test_hello_world() -> None:
    assert convert("Hello, world!", case.UPPER) == "HELLO, WORLD!"


def test_one_two_three() -> None:
    assert convert("ONE\nTWO\nTHREE", case.TITLE) == "One\ntwo\nthree"
