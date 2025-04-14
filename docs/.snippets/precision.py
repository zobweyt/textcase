import textcase

textcase.title("27-07 my cat")  # 27 07 My Cat
textcase.title("27-07 my cat", boundaries=[textcase.UNDERSCORE], strip_punctuation=False)  # 27-07 my cat
