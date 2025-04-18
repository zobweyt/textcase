from textcase import ACRONYM


def test_acronym_match_true() -> None:
    """Matches strings that start with an acronym."""
    assert ACRONYM.match("AAa") is True
    assert ACRONYM.match("BRown") is True
    assert ACRONYM.match("ÄPfel") is True
    assert ACRONYM.match("ПЕрСпЕкТиВа24") is True
    assert ACRONYM.match("ὈΔυσσεύς") is True
    assert ACRONYM.match("DEep ORANGE") is True


def test_acronym_match_false() -> None:
    """Does not match strings that do not start with an acronym."""
    assert ACRONYM.match("") is False
    assert ACRONYM.match("a") is False
    assert ACRONYM.match("A") is False
    assert ACRONYM.match("Aa") is False
    assert ACRONYM.match("aaA") is False
    assert ACRONYM.match("1Aa") is False
    assert ACRONYM.match("A42") is False
    assert ACRONYM.match("_") is False
    assert ACRONYM.match("-") is False
    assert ACRONYM.match(" ") is False
    assert ACRONYM.match(".") is False
    assert ACRONYM.match("/") is False
    assert ACRONYM.match(".brown") is False
    assert ACRONYM.match("/BROWN") is False
    assert ACRONYM.match("BROWn") is False
    assert ACRONYM.match("LLMCache") is False
    assert ACRONYM.match("GranatÄpfel") is False
    assert ACRONYM.match("ПЕРСПЕКТИВА24") is False
    assert ACRONYM.match("ὈΔΥΣΣΕΎΣ") is False
    assert ACRONYM.match("deep orange") is False
    assert ACRONYM.match("Hello, world!") is False


def test_acronym_start() -> None:
    """Has a start value of 1."""
    assert ACRONYM.start == 1


def test_acronym_length() -> None:
    """Has a length value of 0."""
    assert ACRONYM.length == 0
