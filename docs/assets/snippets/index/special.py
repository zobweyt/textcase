from textcase import case, convert

print(convert("E5150", case.SNAKE))  # e_5150
print(convert("10,000Days", case.SNAKE))  # 10,000_days
print(convert("Hello, world!", case.UPPER))  # HELLO, WORLD!
print(convert("ONE\nTWO\nTHREE", case.TITLE))  # One\ntwo\nthree
