from textcase import Case

dot = Case(delimiter=".", transform=lambda words: map(str.lower, words))


def test_custom_case_convert() -> None:
    assert dot("Dot case var") == "dot.case.var"


def test_custom_case_is_case() -> None:
    assert dot.match("dot.case.var") is True
    assert dot.match("Dot case var") is False
