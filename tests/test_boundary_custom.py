from textcase import Boundary, title


def test_boundary_from_delimiter() -> None:
    assert title("coolers.revenge", boundaries=[Boundary.from_delimiter(".")]) == "Coolers Revenge"


def test_boundary_init() -> None:
    AT_LETTER = Boundary(
        match=lambda text: (len(text) > 1 and text[0] == "@") and (text[1] == text[1].lower()),
        start=1,
        length=0,
    )

    assert title("name@domain", boundaries=[AT_LETTER], strip_punctuation=False) == "Name@ Domain"
