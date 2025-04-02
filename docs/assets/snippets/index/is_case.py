from textcase import case, is_case

print(is_case("css-class-name", case.KEBAB))  # True
print(is_case("css-class-name", case.SNAKE))  # False
print(is_case("UPPER_CASE_VAR", case.SNAKE))  # False
