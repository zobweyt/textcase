from textcase import case, convert

print(repr(convert("E5150", case.SNAKE)))
print(repr(convert("10,000Days", case.SNAKE)))
print(repr(convert("Hello, world!", case.UPPER)))
print(repr(convert("ONE\nTWO\nTHREE", case.TITLE)))
