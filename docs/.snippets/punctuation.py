import textcase

textcase.snake("E5150")  # e_5150
textcase.title("ONE\nTWO")  # One\ntwo
textcase.snake("10,000Days")  # 10000_days

textcase.upper("Hello, world!")  # HELLO WORLD
textcase.upper("Hello, world!", strip_punctuation=False)  # HELLO, WORLD!
