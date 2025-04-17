from textcase import Boundary, title


def test_boundary_from_delimiter() -> None:
    assert title("coolers.revenge", boundaries=[Boundary.from_delimiter(".")]) == "Coolers Revenge"


def test_boundary_init() -> None:
    AT_LETTER = Boundary(match=lambda s: s[:1] == "@" and s[:2] == s[:2].lower(), start=1)

    assert title("name@domain", boundaries=[AT_LETTER], strip_punctuation=False) == "Name@ Domain"
