# Границы

## Специфичность границ

Бывает сложно определить, как разбить строку на слова. Вот почему [`convert`](../reference/convert.md/) использует набор [границ слов по умолчанию](../reference/boundary.md/#textcase.boundary.DEFAULT_BOUNDARIES), но иногда этого недостаточно для удовлетворения конкретного варианта использования.

Допустим, строка имеет слово `2D`, например `scale2D`. Никакого специального использования [`convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) будет недостаточно для решения проблемы. В этом случае мы можем дополнительно указать, по каким границам разбивать строку. Эта библиотека предоставляет некоторые [шаблоны для достижения этой специфичности](../reference/boundary.md/#textcase.boundary). Мы можем указать, по каким границам мы хотим разбить, используя экземпляры класса [`Boundary`](../reference/boundary.md/#textcase.boundary.Boundary):

```python exec="true" source="tabbed-left" tabs="specificity.py|output.txt" result="txt" hl_lines="7"
--8<-- "docs/.snippets/boundaries/specificity.py"
```

## Кастомные границы

Эта библиотека предоставляет [ряд констант для границ](../reference/boundary.md/#textcase.boundary), связанных с общими случаями. Но вы можете создать свою собственную границу для разбиения по другим критериям:

```python exec="true" source="tabbed-left" tabs="custom.py|output.txt" result="txt" hl_lines="8-11 16-20"
--8<-- "docs/.snippets/boundaries/custom.py"
```

Чтобы узнать больше о создании кастомной границы с нуля, взгляните на класс [`textcase.boundary.Boundary`](../reference/boundary.md/#textcase.boundary.Boundary).
