# Границы

## Специфичность границ

Может быть сложно определить, как разбить строку на слова. Вот почему этот случай предоставляет функциональность [`convert`](../reference/convert.md/) и [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert), но иногда этого недостаточно для удовлетворения конкретного варианта использования.

Допустим, идентификатор имеет слово `2D`, например `scale2D`. Никакого исключительного использования [`convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) или [`CaseConverter.convert`](../reference/converter.md/#textcase.converter.CaseConverter.convert) будет недостаточно для решения проблемы. В этом случае мы можем дополнительно указать, по каким границам разбивать строку. Эта библиотека предоставляет некоторые шаблоны для достижения этой специфичности. Мы можем указать, по каким границам мы хотим разбить, используя экземпляры класса [`Boundary`](../reference/boundary.md/#textcase.boundary.Boundary):

```python
--8<-- "assets/snippets/boundaries/specificity.py"
```

## Кастомные границы

Эта библиотека предоставляет ряд констант для границ, связанных с общими случаями. Но вы можете создать свою собственную границу для разбиения по другим критериям:

```python
--8<-- "assets/snippets/boundaries/custom.py"
```

Чтобы узнать больше о построении границы с нуля, взгляните на класс [`textcase.boundary.Boundary`](../reference/boundary.md/#textcase.boundary.Boundary).
