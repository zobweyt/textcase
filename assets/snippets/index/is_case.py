from textcase import case, is_case

print(is_case("css-class-name", case.KEBAB))
print(is_case("css-class-name", case.SNAKE))
print(is_case("UPPER_CASE_VAR", case.SNAKE))
