from textcase import Boundary

AT_LOWER = Boundary(match=lambda s: s[:1] == "@" and s[:2].islower(), start=1)


def test_at_lower_match_true() -> None:
    """Matches strings that start with an at-lower combination."""
    assert AT_LOWER.match("@d") is True
    assert AT_LOWER.match("@dOMAIN") is True
    assert AT_LOWER.match("@domain.com") is True
    assert AT_LOWER.match("@äpfel.") is True
    assert AT_LOWER.match("@пЕРСПЕКТИВА24_") is True
    assert AT_LOWER.match("@ὀδυσσεύς") is True


def test_at_lower_match_false() -> None:
    """Does not match strings that do not start with an at-lower combination."""
    assert AT_LOWER.match("") is False
    assert AT_LOWER.match("a") is False
    assert AT_LOWER.match("A") is False
    assert AT_LOWER.match("aA") is False
    assert AT_LOWER.match("Aa") is False
    assert AT_LOWER.match("ÄAa") is False
    assert AT_LOWER.match("1ä") is False
    assert AT_LOWER.match("1Ὀa") is False
    assert AT_LOWER.match("п42") is False
    assert AT_LOWER.match("Σ1") is False
    assert AT_LOWER.match("_") is False
    assert AT_LOWER.match("-") is False
    assert AT_LOWER.match(" ") is False
    assert AT_LOWER.match("·") is False
    assert AT_LOWER.match("/") is False
    assert AT_LOWER.match("_brown") is False
    assert AT_LOWER.match("/BROWN") is False
    assert AT_LOWER.match("brown.") is False
    assert AT_LOWER.match("LLMCache.") is False
    assert AT_LOWER.match("GranatÄpfel.") is False
    assert AT_LOWER.match("ПЕРСПЕКТИВА24.") is False
    assert AT_LOWER.match("ὈΔΥΣΣΕΎΣ.") is False
    assert AT_LOWER.match("deep_orange..") is False
    assert AT_LOWER.match("Hello, world!") is False


def test_at_lower_start() -> None:
    """Has a start value of 1."""
    assert AT_LOWER.start == 1


def test_at_lower_length() -> None:
    """Has a length value of 0."""
    assert AT_LOWER.length == 0
