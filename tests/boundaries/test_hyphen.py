from textcase import HYPHEN


def test_hyphen_match_true() -> None:
    """Matches strings that start with a hyphen."""
    assert HYPHEN.match("-") is True
    assert HYPHEN.match("-brown") is True
    assert HYPHEN.match("-LLMCache") is True
    assert HYPHEN.match("-GranatÄpfel") is True
    assert HYPHEN.match("-ПЕРСПЕКТИВА24") is True
    assert HYPHEN.match("-ὈΔΥΣΣΕΎΣ") is True
    assert HYPHEN.match("--deep-orange") is True


def test_hyphen_match_false() -> None:
    """Does not match strings that do not start with a hyphen."""
    assert HYPHEN.match("") is False
    assert HYPHEN.match("a") is False
    assert HYPHEN.match("A") is False
    assert HYPHEN.match("aA") is False
    assert HYPHEN.match("Aa") is False
    assert HYPHEN.match("ÄAa") is False
    assert HYPHEN.match("1ä") is False
    assert HYPHEN.match("1Ὀa") is False
    assert HYPHEN.match("п42") is False
    assert HYPHEN.match("Σ1") is False
    assert HYPHEN.match("_") is False
    assert HYPHEN.match(" ") is False
    assert HYPHEN.match("·") is False
    assert HYPHEN.match(".") is False
    assert HYPHEN.match("/") is False
    assert HYPHEN.match(".brown") is False
    assert HYPHEN.match("/BROWN") is False
    assert HYPHEN.match("brown-") is False
    assert HYPHEN.match("LLMCache-") is False
    assert HYPHEN.match("GranatÄpfel-") is False
    assert HYPHEN.match("ПЕРСПЕКТИВА24-") is False
    assert HYPHEN.match("ὈΔΥΣΣΕΎΣ-") is False
    assert HYPHEN.match("deep-orange--") is False
    assert HYPHEN.match("Hello, world!") is False


def test_hyphen_start() -> None:
    """Has a start value of 0."""
    assert HYPHEN.start == 0


def test_hyphen_length() -> None:
    """Has a length value of 1."""
    assert HYPHEN.length == 1
