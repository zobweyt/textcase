# Конвертер

## Класс преобразователя регистра

Преобразование регистра происходит в две части. Первая часть разделяет идентификатор на ряд слов, а вторая объединяет слова обратно. Каждый из этих шагов определяется с помощью функций [`CaseConverter.from_case`][textcase.converter.CaseConverter.from_case] и [`CaseConverter.to_case`][textcase.converter.CaseConverter.to_case] соответственно.

[`CaseConverter`][textcase.converter.CaseConverter] — это класс, который инкапсулирует границы, используемые для разделения, а также шаблон и разделитель для мутации и объединения. Метод [`CaseConverter.convert`][textcase.converter.CaseConverter.convert] применит границы, шаблон и разделитель соответствующим образом. Это позволяет заранее определить параметры для преобразования регистра:

```python exec="true" source="tabbed-left" tabs="converter.py|output.txt" result="txt"
--8<-- "docs/.snippets/converter/converter.py"
```

Более подробную информацию о том, как преобразуются строки, см. в документации по [textcase.converter.CaseConverter][].
