from textcase import case, convert


def test_german() -> None:
    assert convert("GranatÄpfel", case.KEBAB) == "granat-äpfel"


def test_russian() -> None:
    assert convert("ПЕРСПЕКТИВА24", case.TITLE) == "Перспектива 24"


def test_ancient_greek() -> None:
    assert convert("ὈΔΥΣΣΕΎΣ", case.LOWER) == "ὀδυσσεύς"
