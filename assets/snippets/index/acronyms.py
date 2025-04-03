from textcase import case, convert

print(convert("IOStream", case.SNAKE))
print(convert("myJSONParser", case.SNAKE))
print(convert("__weird--var _name-", case.SNAKE))
