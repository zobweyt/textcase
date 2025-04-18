from textcase import UNDERSCORE


def test_underscore_match_true() -> None:
    """Matches strings that start with an underscore."""
    assert UNDERSCORE.match("_") is True
    assert UNDERSCORE.match("_brown") is True
    assert UNDERSCORE.match("_LLMCache") is True
    assert UNDERSCORE.match("_GranatÄpfel") is True
    assert UNDERSCORE.match("_ПЕРСПЕКТИВА24") is True
    assert UNDERSCORE.match("_ὈΔΥΣΣΕΎΣ") is True
    assert UNDERSCORE.match("__deep_orange") is True


def test_underscore_match_false() -> None:
    """Does not match strings that do not start with an underscore."""
    assert UNDERSCORE.match("") is False
    assert UNDERSCORE.match("a") is False
    assert UNDERSCORE.match("A") is False
    assert UNDERSCORE.match("aA") is False
    assert UNDERSCORE.match("Aa") is False
    assert UNDERSCORE.match("ÄAa") is False
    assert UNDERSCORE.match("1ä") is False
    assert UNDERSCORE.match("1Ὀa") is False
    assert UNDERSCORE.match("п42") is False
    assert UNDERSCORE.match("Σ1") is False
    assert UNDERSCORE.match("-") is False
    assert UNDERSCORE.match(" ") is False
    assert UNDERSCORE.match("·") is False
    assert UNDERSCORE.match(".") is False
    assert UNDERSCORE.match("/") is False
    assert UNDERSCORE.match(".brown") is False
    assert UNDERSCORE.match("/BROWN") is False
    assert UNDERSCORE.match("brown_") is False
    assert UNDERSCORE.match("LLMCache_") is False
    assert UNDERSCORE.match("GranatÄpfel_") is False
    assert UNDERSCORE.match("ПЕРСПЕКТИВА24_") is False
    assert UNDERSCORE.match("ὈΔΥΣΣΕΎΣ_") is False
    assert UNDERSCORE.match("deep_orange__") is False
    assert UNDERSCORE.match("Hello, world!") is False


def test_underscore_start() -> None:
    """Has a start value of 0."""
    assert UNDERSCORE.start == 0


def test_underscore_length() -> None:
    """Has a length value of 1."""
    assert UNDERSCORE.length == 1
