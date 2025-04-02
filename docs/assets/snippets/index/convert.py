from textcase import case, convert

print(convert("ronnie james dio", case.SNAKE))  # ronnie_james_dio
print(convert("Ronnie_James_dio", case.CONSTANT))  # RONNIE_JAMES_DIO
print(convert("RONNIE_JAMES_DIO", case.KEBAB))  # ronnie-james-dio
print(convert("RONNIE-JAMES-DIO", case.CAMEL))  # ronnieJamesDio
print(convert("ronnie-james-dio", case.PASCAL))  # RonnieJamesDio
print(convert("RONNIE JAMES DIO", case.LOWER))  # ronnie james dio
print(convert("ronnie james dio", case.UPPER))  # RONNIE JAMES DIO
print(convert("ronnie-james-dio", case.TITLE))  # Ronnie James Dio
print(convert("ronnie james dio", case.SENTENCE))  # Ronnie james dio
