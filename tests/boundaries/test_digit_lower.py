from textcase import DIGIT_LOWER


def test_digit_lower_match_true() -> None:
    """Matches strings that start with a digit-lower combination."""
    assert DIGIT_LOWER.match("1a") is True
    assert DIGIT_LOWER.match("1aA") is True
    assert DIGIT_LOWER.match("8a") is True
    assert DIGIT_LOWER.match("0b99") is True
    assert DIGIT_LOWER.match("4ä2") is True
    assert DIGIT_LOWER.match("9п7") is True
    assert DIGIT_LOWER.match("5ὀ2") is True
    assert DIGIT_LOWER.match("4d7 78") is True


def test_digit_lower_match_false() -> None:
    """Does not match strings that do not start with a digit-lower combination."""
    assert DIGIT_LOWER.match("") is False
    assert DIGIT_LOWER.match("a") is False
    assert DIGIT_LOWER.match("A") is False
    assert DIGIT_LOWER.match("aA") is False
    assert DIGIT_LOWER.match("Aa") is False
    assert DIGIT_LOWER.match("ÄAa") is False
    assert DIGIT_LOWER.match("1Ὀa") is False
    assert DIGIT_LOWER.match("п42") is False
    assert DIGIT_LOWER.match("Σ1") is False
    assert DIGIT_LOWER.match("_") is False
    assert DIGIT_LOWER.match("-") is False
    assert DIGIT_LOWER.match(" ") is False
    assert DIGIT_LOWER.match(".") is False
    assert DIGIT_LOWER.match("/") is False
    assert DIGIT_LOWER.match(".brown") is False
    assert DIGIT_LOWER.match("/BROWN") is False
    assert DIGIT_LOWER.match("BROWn") is False
    assert DIGIT_LOWER.match("LLMCache") is False
    assert DIGIT_LOWER.match("GranatÄpfel") is False
    assert DIGIT_LOWER.match("ПЕРСПЕКТИВА24") is False
    assert DIGIT_LOWER.match("ὈΔΥΣΣΕΎΣ") is False
    assert DIGIT_LOWER.match("deep orange") is False
    assert DIGIT_LOWER.match("Hello, world!") is False


def test_digit_lower_start() -> None:
    """Has a start value of 1."""
    assert DIGIT_LOWER.start == 1


def test_digit_lower_length() -> None:
    """Has a length value of 0."""
    assert DIGIT_LOWER.length == 0
