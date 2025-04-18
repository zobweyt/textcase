from textcase import UPPER_LOWER


def test_upper_lower_match_true() -> None:
    """Matches strings that start with a upper-lower combination."""
    assert UPPER_LOWER.match("Aa") is True
    assert UPPER_LOWER.match("Aaa") is True
    assert UPPER_LOWER.match("AaA") is True
    assert UPPER_LOWER.match("Brown") is True
    assert UPPER_LOWER.match("ÄpfEL") is True
    assert UPPER_LOWER.match("ПеРсПеКтИвА24") is True
    assert UPPER_LOWER.match("ὈδΥΣΣΕΎΣ") is True
    assert UPPER_LOWER.match("Deep orange") is True
    assert UPPER_LOWER.match("Hello, world!") is True


def test_upper_lower_match_false() -> None:
    """Does not match strings that do not start with a upper-lower combination."""
    assert UPPER_LOWER.match("") is False
    assert UPPER_LOWER.match("a") is False
    assert UPPER_LOWER.match("A") is False
    assert UPPER_LOWER.match("aA") is False
    assert UPPER_LOWER.match("ÄAa") is False
    assert UPPER_LOWER.match("1ä") is False
    assert UPPER_LOWER.match("1Ὀa") is False
    assert UPPER_LOWER.match("п42") is False
    assert UPPER_LOWER.match("Σ1") is False
    assert UPPER_LOWER.match("_") is False
    assert UPPER_LOWER.match("-") is False
    assert UPPER_LOWER.match(" ") is False
    assert UPPER_LOWER.match(".") is False
    assert UPPER_LOWER.match("/") is False
    assert UPPER_LOWER.match(".brown") is False
    assert UPPER_LOWER.match("/BROWN") is False
    assert UPPER_LOWER.match("browN") is False
    assert UPPER_LOWER.match("LLMCache") is False
    assert UPPER_LOWER.match("gRANATäPFEL") is False
    assert UPPER_LOWER.match("ПЕРСПЕКТИВА24") is False
    assert UPPER_LOWER.match("ὈΔΥΣΣΕΎΣ") is False
    assert UPPER_LOWER.match("deep orange") is False


def test_upper_lower_start() -> None:
    """Has a start value of 1."""
    assert UPPER_LOWER.start == 1


def test_upper_lower_length() -> None:
    """Has a length value of 0."""
    assert UPPER_LOWER.length == 0
