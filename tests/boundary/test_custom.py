from textcase import case, convert
from textcase.boundary import Boundary


def test_boundary_from_delimiter() -> None:
    assert convert("coolers.revenge", case.TITLE, (Boundary.from_delimiter("."),)) == "Coolers Revenge"


def test_boundary_init() -> None:
    AT_LETTER = Boundary(
        satisfies=lambda text: (len(text) > 1 and text[0] == "@") and (text[1] == text[1].lower()),
        start=1,
        length=0,
    )

    assert convert("name@domain", case.TITLE, (AT_LETTER,)) == "Name@ Domain"
