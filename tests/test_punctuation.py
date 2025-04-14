import textcase


def test_strip_punctuation() -> None:
    assert textcase.snake("E5150") == "e_5150"
    assert textcase.title("ONE\nTWO") == "One\ntwo"
    assert textcase.snake("10,000Days") == "10000_days"
    assert textcase.upper("Hello, world!") == "HELLO WORLD"
    assert textcase.upper("Hello, world!", strip_punctuation=False) == "HELLO, WORLD!"
