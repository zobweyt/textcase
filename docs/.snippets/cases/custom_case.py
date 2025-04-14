from textcase import Case

dot = Case(delimiter=".", transform=lambda words: map(str.lower, words))

dot("Dot case var")  # dot.case.var (1)

dot.match("dot.case.var")  # True (2)
dot.match("Dot case var")  # False (3)
