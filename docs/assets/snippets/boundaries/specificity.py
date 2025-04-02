from textcase import boundary, case, convert

# Not quite what we want
print(convert("scale2D", case.SNAKE, case.CAMEL.boundaries))  # scale_2_d

# Write boundaries explicitly
print(convert("scale2D", case.SNAKE, (boundary.LOWER_DIGIT,)))  # scale_2d
