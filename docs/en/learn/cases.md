# Cases

In fact, [`snake`][textcase.snake], [`kebab`][textcase.kebab], etc. **are not functions**.
They are instances of the [`Case`][textcase.Case] class which has implemented the
[`object.__call__`][object.__call__] dunder method for convenience: [`Case.__call__`][textcase.Case.__call__].
This declarative syntax allows flexibly describe text cases while maintaining all functionality.

You can see a complete list of all built-in cases in the [API Reference][textcase].

??? note "How the case conversion works?"

    The case conversion happens in three steps:

    1. **Splitting**:
       the input `text` is divided into words by scanning for boundaries.
       Boundaries are conditions (or delimiters) that signal where one word ends and another begins.
       For instance, a boundary might detect an [underscore][textcase.UNDERSCORE],
       a [change from lowercase to uppercase][textcase.LOWER_UPPER],
       or even a [digit-to-letter][textcase.DIGIT_LOWER] transition.
       Each time a boundary is detected, the string is split at that position.
    2. **Transforming**:
       once the `text` is split into words, the [`transform`][textcase.Case.transform] is applied.
       This function ([which you can customize](#creating-custom-cases)) determines how each word will be transformed.
       For instance, [lowercase][str.lower] conversion, [capitalization][str.capitalize],
       or an entirely [custom transformation](#creating-custom-cases) can be applied to each word.
    3. **Joining**:
       finally, the transformed words are [joined][str.join] back together using
       a defined [`delimiter`][textcase.Case.delimiter]. This [`delimiter`][textcase.Case.delimiter]
       is specific to the case style (for example, underscores (`#!py "_"`)
       for [`snake`][textcase.snake] case or hyphens (`#!py "-"`) for [`kebab`][textcase.kebab] case).

    The result is the input text converted into the desired case.

## Creating Custom Cases

Simular to [`Boundary`][textcase.Boundary], there is the [`Case`][textcase.Case] class
that allows you to define a custom case that behaves like a built-in one:

```py title="cases/custom_case.py" linenums="1" hl_lines="5 7-8"
--8<-- "docs/.snippets/cases/custom_case.py"
```

1. :smile: Since `dot` is an instance of [Case][textcase.Case], it already converts text to the dot case—just
   [call][textcase.Case.__call__] it like a function! :tada:
2. :smile: With `dot`, you don't need to write a custom function to test for the case;
   just use its [`match`][textcase.Case.match] method! :tada:
3. :smile: Again, leveraging `dot`'s [match][textcase.Case.match] method, you can easily verify
   if a string is in the dot case without any extra code! :tada:

To learn more about building a custom case from scratch, take a look at the [`Case`][textcase.Case] class.
