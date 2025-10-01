from textcase import Boundary

DOT = Boundary.from_delimiter(".")


def test_dot_match_true() -> None:
    """Matches strings that start with a dot."""
    assert DOT.match(".") is True
    assert DOT.match(".brown") is True
    assert DOT.match(".LLMCache") is True
    assert DOT.match(".GranatÄpfel") is True
    assert DOT.match(".ПЕРСПЕКТИВА24") is True
    assert DOT.match(".ὈΔΥΣΣΕΎΣ") is True
    assert DOT.match("..deep.orange") is True


def test_dot_match_false() -> None:
    """Does not match strings that do not start with a dot."""
    assert DOT.match("") is False
    assert DOT.match("a") is False
    assert DOT.match("A") is False
    assert DOT.match("aA") is False
    assert DOT.match("Aa") is False
    assert DOT.match("ÄAa") is False
    assert DOT.match("1ä") is False
    assert DOT.match("1Ὀa") is False
    assert DOT.match("п42") is False
    assert DOT.match("Σ1") is False
    assert DOT.match("_") is False
    assert DOT.match("-") is False
    assert DOT.match(" ") is False
    assert DOT.match("·") is False
    assert DOT.match("/") is False
    assert DOT.match("_brown") is False
    assert DOT.match("/BROWN") is False
    assert DOT.match("brown.") is False
    assert DOT.match("LLMCache.") is False
    assert DOT.match("GranatÄpfel.") is False
    assert DOT.match("ПЕРСПЕКТИВА24.") is False
    assert DOT.match("ὈΔΥΣΣΕΎΣ.") is False
    assert DOT.match("deep_orange..") is False
    assert DOT.match("Hello, world!") is False


def test_dot_start() -> None:
    """Has a start value of 0."""
    assert DOT.start == 0


def test_dot_length() -> None:
    """Has a length value of 1."""
    assert DOT.length == 1


def test_return_type_of_custom_subclass() -> None:
    "Verify that method returns an instance of the custom subclass."

    class CustomBoundary(Boundary):
        pass

    assert type(CustomBoundary.from_delimiter(".")).__name__ == CustomBoundary.__name__
