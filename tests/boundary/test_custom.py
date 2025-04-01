from textcase import case, convert
from textcase.boundary import Boundary


def test_custom_simple_boundary() -> None:
    DOT = Boundary(
        satisfies=lambda text: text.startswith("."),
        length=1,
    )

    assert convert("coolers.revenge", case.TITLE, (DOT,)) == "Coolers Revenge"


def test_custom_complex_boundary() -> None:
    AT_LETTER = Boundary(
        satisfies=lambda text: (len(text) > 1 and text[0] == "@") and (text[1] == text[1].lower()),
        start=1,
        length=0,
    )

    assert convert("name@domain", case.TITLE, (AT_LETTER,)) == "Name@ Domain"
