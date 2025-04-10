---
hide:
  - footer
---

<p align="center">
  <span>&emsp;</span>
  <span>&emsp;</span>
  <span>&emsp;</span>
  <a href="https://pypi.python.org/pypi/textcase">
    <img src="https://raw.githubusercontent.com/zobweyt/textcase/refs/heads/main/docs/assets/favicon.svg" alt="textcase logo" width="96" height="96" />
  </a>
</p>

<h1 align="center">
  textcase
</h1>

<p align="center">
  Многофункциональная библиотека преобразования регистра текста в Python.
</p>

<p align="center">
  <a href="https://coveralls.io/github/zobweyt/textcase" target="_blank">
    <img src="https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main" alt="Coveralls"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/badge/dependencies-0-brightgreen" alt="Dependencies"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/v/textcase.svg" alt="PyPI - Version"/>
  </a>
  <a href="https://pypistats.org/packages/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/dm/textcase" alt="PyPI - Downloads"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/textcase.svg" alt="PyPI - Python Version"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/types/textcase" alt="PyPI - Types"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/wheel/textcase" alt="PyPI - Wheel"/>
  </a>
  <a href="https://aur.archlinux.org/packages/python-textcase-git" target="_blank">
    <img src="https://img.shields.io/aur/version/python-textcase-git" alt="AUR Version"/>
  </a>
</p>

## Особенности

- **Преобразование регистров текста**: преобразование строк между различными текстовыми регистрами (например, snake_case, kebab-case, camelCase и т.д.).
- **Масштабируемый дизайн**: легко расширяйте библиотеку с помощью кастомных регистров и границ.
- **Обработка сокращений**: корректно распознаёт и форматирует сокращения в строках (как в `HTTPRequest`).
- **Поддержка не-ASCII**: легко обрабатывает символы, отличные от ASCII (не делается никаких выводов о языке ввода).
- **100%-ный охват тестированием**: всесторонние тесты гарантируют надёжность и корректность.
- **Хорошая документация**: чистая документация с примерами использования для удобства понимания.
- **Высокая производительность**: эффективная реализация без использования регулярных выражений.
- **Нет зависимостей**: библиотека не имеет внешних зависимостей, что делает её лёгкой и понятной для интеграции.

## Установка

<!-- termynal -->

```console
$ pip install textcase
---> 100%
Готово!
```

## Использование

Вы можете преобразовать строки в регистр, используя функцию [`convert`][textcase.convert]:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/.snippets/index/convert.py"
```

По умолчанию [`convert`][textcase.convert] и [`CaseConverter.convert`][textcase.converter] будут делить слова [по заданным по умолчанию границам слов][textcase.boundary.DEFAULT_BOUNDARIES], то есть:

- Подчёркивания: `_`,
- Дефисы: `-`,
- Пробелы: ` `,
- Изменение заглавных букв со строчных на прописны: `aA`,
- Соседние цифры и буквы: `a1`, `1a`, `A1`, `1A`,
- Аббревиатуры и сокращения: `AAa` (как в `HTTPRequest`).

Для большей точности вы можете указать границы для разделения, основываясь на границах слов для конкретного случая. Например, вы можете явно указать какие границы будут использоваться:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt" hl_lines="4"
--8<-- "docs/.snippets/index/precision.py"
```

Эта библиотека может распознавать аббревиатуры и сокращения в строках, подобные тем, что используются в регистре camel. Она также игнорирует любые начальные, конечные или повторяющиеся разделители:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/.snippets/index/acronyms.py"
```

Библиотека также поддерживает символы, отличные от ASCII. **Однако при этом не делается никаких выводов о языке ввода**. Например, в голландском языке орграф "ij" рассматривается как два отдельных символа Unicode и не пишется с заглавной буквы. В отличие от этого, символ "æ" будет написан с заглавной буквы, как и ожидалось. Кроме того, в английском языке текст "I THINK I DO" будет преобразован в "i think i do", а не в "I think I do". Это означает, что библиотека может обрабатывать различные символы:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/.snippets/index/non_ascii.py"
```

По умолчанию символы, за которыми следуют цифры, и наоборот, считаются границами слов. Кроме того, любые специальные символы ASCII (кроме `_` и `-`) игнорируются:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/.snippets/index/special.py"
```

Вы также можете проверить, в каком регистре находится строка:

```python exec="true" source="tabbed-left" tabs="main.py|output.txt" result="txt"
--8<-- "docs/.snippets/index/is_case.py"
```
