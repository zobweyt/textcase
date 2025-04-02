from textcase import CaseConverter, case, pattern

converter = CaseConverter()
converter.pattern = pattern.camel
converter.delimiter = "_"

print(converter.convert("My Special Case"))  # my_Special_Case

converter.from_case(case.CAMEL)
converter.to_case(case.SNAKE)

print(converter.convert("mySpecialCase"))  # my_special_case
