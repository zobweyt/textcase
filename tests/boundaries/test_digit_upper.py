from textcase import DIGIT_UPPER


def test_digit_upper_match_true() -> None:
    """Matches strings that start with a digit-upper combination."""
    assert DIGIT_UPPER.match("1A") is True
    assert DIGIT_UPPER.match("1Aa") is True
    assert DIGIT_UPPER.match("8A") is True
    assert DIGIT_UPPER.match("0B99") is True
    assert DIGIT_UPPER.match("4Ä2") is True
    assert DIGIT_UPPER.match("9П7") is True
    assert DIGIT_UPPER.match("5Ὀ2") is True
    assert DIGIT_UPPER.match("4D7 78") is True


def test_digit_upper_match_false() -> None:
    """Does not match strings that do not start with a digit-upper combination."""
    assert DIGIT_UPPER.match("") is False
    assert DIGIT_UPPER.match("a") is False
    assert DIGIT_UPPER.match("A") is False
    assert DIGIT_UPPER.match("aA") is False
    assert DIGIT_UPPER.match("Aa") is False
    assert DIGIT_UPPER.match("ÄAa") is False
    assert DIGIT_UPPER.match("1ä") is False
    assert DIGIT_UPPER.match("п42") is False
    assert DIGIT_UPPER.match("Σ1") is False
    assert DIGIT_UPPER.match("_") is False
    assert DIGIT_UPPER.match("-") is False
    assert DIGIT_UPPER.match(" ") is False
    assert DIGIT_UPPER.match(".") is False
    assert DIGIT_UPPER.match("/") is False
    assert DIGIT_UPPER.match(".brown") is False
    assert DIGIT_UPPER.match("/BROWN") is False
    assert DIGIT_UPPER.match("BROWn") is False
    assert DIGIT_UPPER.match("LLMCache") is False
    assert DIGIT_UPPER.match("GranatÄpfel") is False
    assert DIGIT_UPPER.match("ПЕРСПЕКТИВА24") is False
    assert DIGIT_UPPER.match("ὈΔΥΣΣΕΎΣ") is False
    assert DIGIT_UPPER.match("deep orange") is False
    assert DIGIT_UPPER.match("Hello, world!") is False


def test_digit_upper_start() -> None:
    """Has a start value of 1."""
    assert DIGIT_UPPER.start == 1


def test_digit_upper_length() -> None:
    """Has a length value of 0."""
    assert DIGIT_UPPER.length == 0
