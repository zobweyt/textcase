from textcase import boundary, case, convert

print(convert("2020-04-16_my_cat_cali", case.TITLE))  # 2020 04 16 My Cat Cali
print(convert("2020-04-16_my_cat_cali", case.TITLE, (boundary.UNDERSCORE,)))  # 2020-04-16 My Cat Cali
