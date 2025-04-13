from textcase import case, convert

print(convert("ronnie james dio", case.SNAKE))
print(convert("Ronnie_James_dio", case.CONSTANT))
print(convert("RONNIE_JAMES_DIO", case.KEBAB))
print(convert("ronnie james dio", case.MIDDOT))
print(convert("RONNIE-JAMES-DIO", case.CAMEL))
print(convert("ronnie-james-dio", case.PASCAL))
print(convert("RONNIE JAMES DIO", case.LOWER))
print(convert("ronnie james dio", case.UPPER))
print(convert("ronnie-james-dio", case.TITLE))
print(convert("ronnie james dio", case.SENTENCE))
