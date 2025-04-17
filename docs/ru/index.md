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
  Python библиотека для преобразования регистра текста.
</p>

<p align="center">
  <a href="https://coveralls.io/github/zobweyt/textcase" target="_blank">
    <img src="https://img.shields.io/coverallsCoverage/github/zobweyt/textcase?branch=main" alt="Coveralls"/>
  </a>
  <a href="https://pypistats.org/packages/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/dm/textcase" alt="PyPI - Downloads"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/v/textcase.svg" alt="PyPI - Version"/>
  </a>
  <a href="https://pypi.python.org/pypi/textcase" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/textcase.svg" alt="PyPI - Python Version"/>
  </a>
</p>

## Особенности

<div class="md-emoji-list" markdown>

- :fire: <span>**Преобразование регистра текста**: [преобразуйте](#использование) строки между различными регистрами текста (например, [snake_case][textcase.snake], [kebab-case][textcase.kebab], [camelCase][textcase.camel] и т.д.).</span>
- :fire: <span>**Расширяемость**: расширяйте библиотеку с помощью кастомных [границ слов](./learn/boundaries.md) и [регистров текста](./learn/cases.md).</span>
- :fire: <span>**Точность**: [находит любые границы слов](#точность) в строках, включая [аббревиатуры и сокращения][textcase.ACRONYM] (как в `#!py "HTTPRequest"`).</span>
- :fire: <span>**Поддержка не-ASCII**: обрабатывает [не-ASCII символы](#не-ascii-символы) без проблем (не делается никаких выводов о самом языке ввода).</span>
- :fire: <span>**Лёгкость, производительность, нет зависимостей**: эффективная библиотека без регулярных выражений, которая остаётся легкой и не имеет внешних зависимостей.</span>
- :fire: <span>**100% <abbr title="Объём кода, который автоматически тестируется">покрытие тестами</abbr>**: каждая строка кода тщательно протестирована на надёжность.</span>
- :fire: <span>**100% <abbr title="Аннотации типов Python, с этим ваш редактор и внешние инструменты могут предоставить вам лучшую поддержку">типизированная</abbr> кодовая база**: полные аннотации типов для лучшего опыта разработки.</span>

</div>

## Установка

<!-- termynal -->

```console
$ pip install textcase
---> 100%
Готово!
```

## Использование

Конвертируйте строки в текстовые регистры:

```py title="cases.py" linenums="1"
--8<-- "docs/.snippets/cases.py"
```

Вы также можете проверить в каком регистре находится строка:

```py title="match.py" linenums="1" hl_lines="3-5"
--8<-- "docs/.snippets/match.py"
```

### Границы

По умолчанию библиотека разделяет слова по заданным по умолчанию границам слов, а именно:

- Подчёркивания: `#!py "_"`,
- Дефисы: `#!py "-"`,
- Пробелы: `#!py " "`,
- Интерпункты: `#!py "·"`,
- Изменение регистра с нижнего на верхний: `#!py "aA"`,
- Соседние цифры и буквы: `#!py "a1"`, `#!py "1a"`, `#!py "A1"`, `#!py "1A"`,
- Аббревиатуры и сокращения: `#!py "AAa"` (как в `#!py "HTTPRequest"`).

Вы можете узнать больше о границах [тут](./learn/boundaries.md).

### Точность

Для большей точности вы можете указать границы для разделения на основе границ слов конкретного случая.
Например, вы можете явно указать, какие границы будут использоваться:

```py title="precision.py" linenums="1" hl_lines="4"
--8<-- "docs/.snippets/precision.py"
```

Эта библиотека может обнаруживать аббревиатуры и сокращения в строках типа camel.
Она также игнорирует любые начальные, конечные или дублирующие разделители:

```py title="acronyms.py" linenums="1" hl_lines="3-5"
--8<-- "docs/.snippets/acronyms.py"
```

### Не-ASCII Символы

Библиотека также поддерживает символы, не входящие в ASCII. **Однако никаких выводов о самом языке ввода не делается**.
Например, в голландском языке диграф `#!py "ij"` обрабатывается как два отдельных символа Unicode и не будет написан заглавными буквами.
Напротив, символ `#!py "æ"` будет написан заглавными буквами, как и ожидалось.
Кроме того, в английском языке текст `#!py "I THINK I DO"` будет преобразован в `#!py "i think i do"`, а не `#!py "I think I do"`.
Это означает, что библиотека может обрабатывать различные символы:

```py title="non_ascii.py" linenums="1" hl_lines="3-5"
--8<-- "docs/.snippets/non_ascii.py"
```

### Пунктуация

По умолчанию символы, за которыми следуют цифры и наоборот, считаются границами слов.
Кроме того, символы [пунктуация][string.punctuation] удаляются
(исключая текущий регистр [`delimiter`][textcase.Case.delimiter]), а другие специальные символы игнорируются.
Вы можете управлять этим поведением с помощью аргумента `strip_punctuation`:

```py title="punctuation.py" linenums="1" hl_lines="7-8"
--8<-- "docs/.snippets/punctuation.py"
```
