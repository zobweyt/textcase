# textcase

[![Coveralls](https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main)](https://coveralls.io/github/zobweyt/textcase)
[![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)](https://pypi.python.org/pypi/textcase)
[![PyPI - Version](https://img.shields.io/pypi/v/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/textcase.svg)](https://pypi.python.org/pypi/textcase)
[![PyPI - Types](https://img.shields.io/pypi/types/textcase)](https://pypi.python.org/pypi/textcase)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/textcase)](https://pypi.python.org/pypi/textcase)
[![AUR Version](https://img.shields.io/aur/version/python-textcase-git)](https://aur.archlinux.org/packages/python-textcase-git)

Многофункциональная библиотека преобразования регистра текста в Python.

## Особенности

- **Преобразование регистров текста**: Преобразование строк между различными текстовыми регистрами (например, snake_case, kebab-case, camelCase и т.д.).
- **Масштабируемый дизайн**: Легко расширяйте библиотеку с помощью пользовательских регистров и границ.
- **Обработка сокращений**: Корректно распознает и форматирует сокращения в строках (как в `HTTPRequest`).
- **Поддержка не-ASCII**: Легко обрабатывает символы, отличные от ASCII (не делается никаких выводов о языке ввода).
- **100%-ный охват тестированием**: Всесторонние тесты гарантируют надежность и корректность.
- **Хорошо документированная**: Чистая документация с примерами использования для удобства понимания.
- **Высокая производительность**: Эффективная реализация без использования регулярных выражений.
- **Нет зависимостей**: Библиотека не имеет внешних зависимостей, что делает ее легкой и понятной для интеграции.

## Установка

<!-- termynal -->

```console
$ pip install textcase
---> 100%
Готово!
```

## Использование

Вы можете преобразовать строки в регистр, используя функцию [`convert`](./reference/convert.md/):

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/convert.py"
```

По умолчанию [`convert`](./reference/convert.md/) и [`CaseConverter.convert`](./reference/converter.md/#textcase.converter) будут делить слова [по заданным по умолчанию границам слов](./reference/boundary.md/#textcase.boundary.DEFAULT_BOUNDARIES), то есть:

- подчеркивания `_`,
- дефисы `-`,
- пробелы ` `,
- изменение заглавных букв со строчных на прописны `aA`,
- соседние цифры и буквы `a1`, `1a`, `A1`, `1A`,
- и акроиннменты `AAa` (как в `HTTPRequest`).

Для большей точности вы можете указать границы для разделения, основываясь на границах слов в конкретном падеже. Например, при разделении из падежа snake в качестве границ слов будут использоваться только символы подчеркивания:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt" hl_lines="4"
--8<-- "docs/assets/snippets/index/precision.py"
```

Эта библиотека может распознавать сокращения в строках, подобных camel. Она также игнорирует любые начальные, конечные или повторяющиеся разделители:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/acronyms.py"
```

Библиотека также поддерживает символы, отличные от ASCII. Однако при этом не делается никаких выводов о языке ввода. Например, в голландском языке орграф "ij" рассматривается как два отдельных символа Unicode и не пишется с заглавной буквы. В отличие от этого, символ "æ" будет написан с заглавной буквы, как и ожидалось. Кроме того, в английском языке текст "I THINK I DO" будет преобразован в "i think i do", а не в "I think I do". Это означает, что библиотека может обрабатывать различные символы:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/non_ascii.py"
```

По умолчанию символы, за которыми следуют цифры, и наоборот, считаются границами слов. Кроме того, любые специальные символы ASCII (кроме "_" и "-") игнорируются:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/special.py"
```

Вы также можете проверить, в каком регистре находится строка в:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/assets/snippets/index/is_case.py"
```
