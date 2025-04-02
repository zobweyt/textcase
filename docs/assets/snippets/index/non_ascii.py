from textcase import case, convert

print(convert("GranatÄpfel", case.KEBAB))  # granat-äpfel
print(convert("ПЕРСПЕКТИВА24", case.TITLE))  # Перспектива 24
print(convert("ὈΔΥΣΣΕΎΣ", case.LOWER))  # ὀδυσσεύς
