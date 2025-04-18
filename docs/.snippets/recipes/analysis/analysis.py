import csv

from textcase import ACRONYM, Boundary, snake

SCOPE = Boundary.from_delimiter("::")

with open("input.csv") as file:
    reader = csv.DictReader(file)
    reader.fieldnames = tuple(snake(column, boundaries=(ACRONYM, SCOPE)) for column in reader.fieldnames or ())

    print(*reader.fieldnames, sep=",")

    for row in reader:
        print(*map(row.get, reader.fieldnames), sep=",")
