from textcase import UPPER_DIGIT


def test_upper_digit_match_true() -> None:
    """Matches strings that start with a upper-digit combination."""
    assert UPPER_DIGIT.match("A1") is True
    assert UPPER_DIGIT.match("A11") is True
    assert UPPER_DIGIT.match("A8") is True
    assert UPPER_DIGIT.match("B099") is True
    assert UPPER_DIGIT.match("Ä42") is True
    assert UPPER_DIGIT.match("П97") is True
    assert UPPER_DIGIT.match("Ὀ52") is True
    assert UPPER_DIGIT.match("D47 78") is True


def test_upper_digit_match_false() -> None:
    """Does not match strings that do not start with a upper-digit combination."""
    assert UPPER_DIGIT.match("") is False
    assert UPPER_DIGIT.match("a") is False
    assert UPPER_DIGIT.match("A") is False
    assert UPPER_DIGIT.match("aA") is False
    assert UPPER_DIGIT.match("Aa") is False
    assert UPPER_DIGIT.match("ÄAa") is False
    assert UPPER_DIGIT.match("1ä") is False
    assert UPPER_DIGIT.match("1Ὀa") is False
    assert UPPER_DIGIT.match("п42") is False
    assert UPPER_DIGIT.match("_") is False
    assert UPPER_DIGIT.match("-") is False
    assert UPPER_DIGIT.match(" ") is False
    assert UPPER_DIGIT.match(".") is False
    assert UPPER_DIGIT.match("/") is False
    assert UPPER_DIGIT.match(".brown") is False
    assert UPPER_DIGIT.match("/BROWN") is False
    assert UPPER_DIGIT.match("BROWn") is False
    assert UPPER_DIGIT.match("LLMCache") is False
    assert UPPER_DIGIT.match("GranatÄpfel") is False
    assert UPPER_DIGIT.match("ПЕРСПЕКТИВА24") is False
    assert UPPER_DIGIT.match("ὈΔΥΣΣΕΎΣ") is False
    assert UPPER_DIGIT.match("deep orange") is False
    assert UPPER_DIGIT.match("Hello, world!") is False


def test_upper_digit_start() -> None:
    """Has a start value of 1."""
    assert UPPER_DIGIT.start == 1


def test_upper_digit_length() -> None:
    """Has a length value of 0."""
    assert UPPER_DIGIT.length == 0
