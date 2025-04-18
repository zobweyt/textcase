from textcase import SPACE


def test_space_match_true() -> None:
    """Matches strings that start with a space."""
    assert SPACE.match(" ") is True
    assert SPACE.match(" brown") is True
    assert SPACE.match(" LLMCache") is True
    assert SPACE.match(" GranatÄpfel") is True
    assert SPACE.match(" ПЕРСПЕКТИВА24") is True
    assert SPACE.match(" ὈΔΥΣΣΕΎΣ") is True
    assert SPACE.match("  deep orange") is True


def test_space_match_false() -> None:
    """Does not match strings that do not start with a space."""
    assert SPACE.match("") is False
    assert SPACE.match("a") is False
    assert SPACE.match("A") is False
    assert SPACE.match("aA") is False
    assert SPACE.match("Aa") is False
    assert SPACE.match("ÄAa") is False
    assert SPACE.match("1ä") is False
    assert SPACE.match("1Ὀa") is False
    assert SPACE.match("п42") is False
    assert SPACE.match("Σ1") is False
    assert SPACE.match("_") is False
    assert SPACE.match("-") is False
    assert SPACE.match("·") is False
    assert SPACE.match(".") is False
    assert SPACE.match("/") is False
    assert SPACE.match(".brown") is False
    assert SPACE.match("/BROWN") is False
    assert SPACE.match("brown ") is False
    assert SPACE.match("LLMCache ") is False
    assert SPACE.match("GranatÄpfel ") is False
    assert SPACE.match("ПЕРСПЕКТИВА24 ") is False
    assert SPACE.match("ὈΔΥΣΣΕΎΣ ") is False
    assert SPACE.match("deep orange ") is False
    assert SPACE.match("Hello, world!") is False


def test_space_start() -> None:
    """Has a start value of 0."""
    assert SPACE.start == 0


def test_space_length() -> None:
    """Has a length value of 1."""
    assert SPACE.length == 1
