from pathlib import Path

import textcase

filenames = (
    "TODO #3 (Draft).md",
    "BigQuery.csv",
    "Résumé2025.DOCX",
    "LLMCache: Кеширование LLM запросов.pptx",
    "The Python 3 Standard Library by Example.pdf",
)

new_filenames = (textcase.kebab(path.stem) + path.suffix.lower() for filename in filenames if (path := Path(filename)))

for filename, new_filename in zip(filenames, new_filenames):
    print(filename, new_filename, sep=",")
