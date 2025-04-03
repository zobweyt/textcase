from textcase import case, convert
from textcase.boundary import Boundary

# Not quite what we want
print(convert("coolers.revenge", case.TITLE))

# Define custom boundary
DOT = Boundary(
    satisfies=lambda text: text.startswith("."),
    length=1,
)

print(convert("coolers.revenge", case.TITLE, (DOT,)))

# Define complex custom boundary
AT_LETTER = Boundary(
    satisfies=lambda text: (len(text) > 1 and text[0] == "@") and (text[1] == text[1].lower()),
    start=1,
    length=0,
)

print(convert("name@domain", case.TITLE, (AT_LETTER,)))
