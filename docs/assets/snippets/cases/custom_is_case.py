from textcase import is_case
from textcase.boundary import Boundary
from textcase.case import Case
from textcase.pattern import lower

# Define custom boundary
DOT = Boundary(
    satisfies=lambda text: text.startswith("."),
    length=1,
)

# Define custom case
DOT_CASE = Case(
    boundaries=(DOT,),
    pattern=lower,
    delimiter=".",
)

print(is_case("dot.case.var", DOT_CASE))  # True
print(is_case("Dot case var", DOT_CASE))  # False
