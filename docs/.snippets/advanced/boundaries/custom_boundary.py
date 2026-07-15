from textcase import Boundary, title

title("colors.brown")  # Colorsbrown (1)

DOT = Boundary.from_delimiter(".")  # (2)!
title("colors.brown", boundaries=[DOT])  # Colors Brown (3)
