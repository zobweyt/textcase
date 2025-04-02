from textcase import boundary


def test_underscore() -> None:
    assert (boundary.UNDERSCORE,) == tuple(boundary.get_boundaries("_"))


def test_hypen() -> None:
    assert (boundary.HYPHEN,) == tuple(boundary.get_boundaries("-"))


def test_space() -> None:
    assert (boundary.SPACE,) == tuple(boundary.get_boundaries(" "))


def test_lower_upper() -> None:
    assert (boundary.LOWER_UPPER,) == tuple(boundary.get_boundaries("aA"))


def test_upper_lower() -> None:
    assert 0 == len(tuple(boundary.get_boundaries("Aa")))


def test_acronym() -> None:
    assert (boundary.ACRONYM,) == tuple(boundary.get_boundaries("AAa"))


def test_lower_digit() -> None:
    assert (boundary.LOWER_DIGIT,) == tuple(boundary.get_boundaries("a1"))


def test_upper_digit() -> None:
    assert (boundary.UPPER_DIGIT,) == tuple(boundary.get_boundaries("A1"))


def test_digit_lower() -> None:
    assert (boundary.DIGIT_LOWER,) == tuple(boundary.get_boundaries("1a"))


def test_digit_upper() -> None:
    assert (boundary.DIGIT_UPPER,) == tuple(boundary.get_boundaries("1A"))
