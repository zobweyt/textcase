from textcase import boundary, case, convert

print(convert("2020-04-16_my_cat_cali", case.TITLE))
print(convert("2020-04-16_my_cat_cali", case.TITLE, (boundary.UNDERSCORE,)))
