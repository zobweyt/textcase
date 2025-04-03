from textcase import convert
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

print(convert("Dot case var", DOT_CASE))
