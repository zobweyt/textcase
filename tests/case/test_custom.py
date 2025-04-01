from textcase import convert, is_case
from textcase.boundary import Boundary
from textcase.case import Case
from textcase.pattern import lower

DOT = Boundary(
    satisfies=lambda text: text.startswith("."),
    length=1,
)

DOT_CASE = Case(
    boundaries=(DOT,),
    pattern=lower,
    delimiter=".",
)


def test_custom_case_convert() -> None:
    assert convert("Dot case var", DOT_CASE) == "dot.case.var"


def test_custom_case_is_case() -> None:
    assert is_case("dot.case.var", DOT_CASE) is True
    assert is_case("Dot case var", DOT_CASE) is False
