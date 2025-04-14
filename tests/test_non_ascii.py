import textcase


def test_german() -> None:
    assert textcase.kebab("GranatÄpfel") == "granat-äpfel"


def test_russian() -> None:
    assert textcase.title("ПЕРСПЕКТИВА24") == "Перспектива 24"


def test_ancient_greek() -> None:
    assert textcase.lower("ὈΔΥΣΣΕΎΣ") == "ὀδυσσεύς"
