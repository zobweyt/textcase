from textcase import INTERPUNCT


def test_interpunct_match_true() -> None:
    """Matches strings that start with a interpunct."""
    assert INTERPUNCT.match("·") is True
    assert INTERPUNCT.match("·brown") is True
    assert INTERPUNCT.match("·LLMCache") is True
    assert INTERPUNCT.match("·GranatÄpfel") is True
    assert INTERPUNCT.match("·ПЕРСПЕКТИВА24") is True
    assert INTERPUNCT.match("·ὈΔΥΣΣΕΎΣ") is True
    assert INTERPUNCT.match("··deep·orange") is True


def test_interpunct_match_false() -> None:
    """Does not match strings that do not start with a interpunct."""
    assert INTERPUNCT.match("") is False
    assert INTERPUNCT.match("a") is False
    assert INTERPUNCT.match("A") is False
    assert INTERPUNCT.match("aA") is False
    assert INTERPUNCT.match("Aa") is False
    assert INTERPUNCT.match("ÄAa") is False
    assert INTERPUNCT.match("1ä") is False
    assert INTERPUNCT.match("1Ὀa") is False
    assert INTERPUNCT.match("п42") is False
    assert INTERPUNCT.match("Σ1") is False
    assert INTERPUNCT.match("_") is False
    assert INTERPUNCT.match("-") is False
    assert INTERPUNCT.match(" ") is False
    assert INTERPUNCT.match(".") is False
    assert INTERPUNCT.match("/") is False
    assert INTERPUNCT.match(".brown") is False
    assert INTERPUNCT.match("/BROWN") is False
    assert INTERPUNCT.match("brown·") is False
    assert INTERPUNCT.match("LLMCache·") is False
    assert INTERPUNCT.match("GranatÄpfel·") is False
    assert INTERPUNCT.match("ПЕРСПЕКТИВА24·") is False
    assert INTERPUNCT.match("ὈΔΥΣΣΕΎΣ·") is False
    assert INTERPUNCT.match("deep·orange·") is False
    assert INTERPUNCT.match("Hello, world!") is False


def test_interpunct_start() -> None:
    """Has a start value of 0."""
    assert INTERPUNCT.start == 0


def test_interpunct_length() -> None:
    """Has a length value of 1."""
    assert INTERPUNCT.length == 1
