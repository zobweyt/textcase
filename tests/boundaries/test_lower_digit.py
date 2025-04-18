from textcase import LOWER_DIGIT


def test_lower_digit_match_true() -> None:
    """Matches strings that start with a lower-digit combination."""
    assert LOWER_DIGIT.match("a1") is True
    assert LOWER_DIGIT.match("a11") is True
    assert LOWER_DIGIT.match("a8") is True
    assert LOWER_DIGIT.match("b099") is True
    assert LOWER_DIGIT.match("ä42") is True
    assert LOWER_DIGIT.match("п97") is True
    assert LOWER_DIGIT.match("ὀ52") is True
    assert LOWER_DIGIT.match("d47 78") is True


def test_lower_digit_match_false() -> None:
    """Does not match strings that do not start with a lower-digit combination."""
    assert LOWER_DIGIT.match("") is False
    assert LOWER_DIGIT.match("a") is False
    assert LOWER_DIGIT.match("A") is False
    assert LOWER_DIGIT.match("aA") is False
    assert LOWER_DIGIT.match("Aa") is False
    assert LOWER_DIGIT.match("ÄAa") is False
    assert LOWER_DIGIT.match("1ä") is False
    assert LOWER_DIGIT.match("1Ὀa") is False
    assert LOWER_DIGIT.match("Σ1") is False
    assert LOWER_DIGIT.match("_") is False
    assert LOWER_DIGIT.match("-") is False
    assert LOWER_DIGIT.match(" ") is False
    assert LOWER_DIGIT.match(".") is False
    assert LOWER_DIGIT.match("/") is False
    assert LOWER_DIGIT.match(".brown") is False
    assert LOWER_DIGIT.match("/BROWN") is False
    assert LOWER_DIGIT.match("BROWn") is False
    assert LOWER_DIGIT.match("LLMCache") is False
    assert LOWER_DIGIT.match("GranatÄpfel") is False
    assert LOWER_DIGIT.match("ПЕРСПЕКТИВА24") is False
    assert LOWER_DIGIT.match("ὈΔΥΣΣΕΎΣ") is False
    assert LOWER_DIGIT.match("deep orange") is False
    assert LOWER_DIGIT.match("Hello, world!") is False


def test_lower_digit_start() -> None:
    """Has a start value of 1."""
    assert LOWER_DIGIT.start == 1


def test_lower_digit_length() -> None:
    """Has a length value of 0."""
    assert LOWER_DIGIT.length == 0
