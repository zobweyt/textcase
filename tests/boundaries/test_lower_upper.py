from textcase import LOWER_UPPER


def test_lower_upper_match_true() -> None:
    """Matches strings that start with a lower-upper combination."""
    assert LOWER_UPPER.match("aA") is True
    assert LOWER_UPPER.match("aAA") is True
    assert LOWER_UPPER.match("aAa") is True
    assert LOWER_UPPER.match("bROWN") is True
    assert LOWER_UPPER.match("äPFel") is True
    assert LOWER_UPPER.match("пЕрСпЕкТиВа24") is True
    assert LOWER_UPPER.match("ὀΔυσσεύς") is True
    assert LOWER_UPPER.match("dEEP ORANGE") is True


def test_lower_upper_match_false() -> None:
    """Does not match strings that do not start with a lower-upper combination."""
    assert LOWER_UPPER.match("") is False
    assert LOWER_UPPER.match("a") is False
    assert LOWER_UPPER.match("A") is False
    assert LOWER_UPPER.match("Aa") is False
    assert LOWER_UPPER.match("ÄAa") is False
    assert LOWER_UPPER.match("1ä") is False
    assert LOWER_UPPER.match("1Ὀa") is False
    assert LOWER_UPPER.match("п42") is False
    assert LOWER_UPPER.match("Σ1") is False
    assert LOWER_UPPER.match("_") is False
    assert LOWER_UPPER.match("-") is False
    assert LOWER_UPPER.match(" ") is False
    assert LOWER_UPPER.match(".") is False
    assert LOWER_UPPER.match("/") is False
    assert LOWER_UPPER.match(".brown") is False
    assert LOWER_UPPER.match("/BROWN") is False
    assert LOWER_UPPER.match("BROWn") is False
    assert LOWER_UPPER.match("LLMCache") is False
    assert LOWER_UPPER.match("GranatÄpfel") is False
    assert LOWER_UPPER.match("ПЕРСПЕКТИВА24") is False
    assert LOWER_UPPER.match("ὈΔΥΣΣΕΎΣ") is False
    assert LOWER_UPPER.match("deep orange") is False
    assert LOWER_UPPER.match("Hello, world!") is False


def test_lower_upper_start() -> None:
    """Has a start value of 1."""
    assert LOWER_UPPER.start == 1


def test_lower_upper_length() -> None:
    """Has a length value of 0."""
    assert LOWER_UPPER.length == 0
