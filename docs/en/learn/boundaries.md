# Boundaries

Boundaries define where a string is divided into words.
They allow you to control how a string is split during conversions between different naming conventions.

Consider an abstract example where the `#!py "_"` character is used as the boundary:

Imagine the string: `#!py "A_B_C"`

Using `#!py "_"` as a boundary, the string is divided into distinct segments: `#!py ["A", "B", "C"]`

## Specificity of Boundaries

It can be difficult to determine how to split a string into words.

Let's say the string contains the word `#!py "2D"`, for example `#!py "scale2D"`,
and we want to translate it to [`snake`][textcase.snake] case.
How do we decide what `boundaries` to use to split this string into words?
Should it be `#!py "scale_2_d"`, `#!py "scale_2d"` or just `#!py "scale2d"`?

By default, the [conversion method][textcase.Case.__call__] uses some predefined `boundaries`,
but sometimes the predefined boundaries are not enough to meet a specific use case, so you can _explicitly_ set
which ones to use by providing instances of the [Boundary][textcase.Boundary] class.

```py title="boundaries/specificity.py" linenums="1" hl_lines="5-6"
--8<-- "docs/.snippets/boundaries/specificity.py"
```

You can see a complete list of all built-in boundaries in the [API Reference][textcase].

## Creating Custom Boundaries

This library provides a number of constants for boundaries associated with common cases.
But if you need to handle more specific cases, you can easily create custom boundaries and use
them as well as built-in ones:

```py title="boundaries/custom_boundary.py" linenums="1" hl_lines="5-6"
--8<-- "docs/.snippets/boundaries/custom_boundary.py"
```

1. :cry: That is quite **not** what we want.
   Since the library does not handle boundary with a dot (`#!py "."`) by [default][textcase.Case.__call__],
   we need to create it _manually_ using the [`Boundary`][textcase.Boundary] class.
2. :smile: To achieve our goal we need to create a _custom_ boundary
   using the [`Boundary.from_delimiter`][textcase.Boundary.from_delimiter] method.
3. :smile: Now we can _explicitly_ set our _custom_ boundary to the [`boundaries`][textcase.Case.__call__]
   argument and it [will be used when splitting text][textcase.Case.__call__]!

To learn more about building a custom boundary from scratch, take a look at the [`Boundary`][textcase.Boundary] class.
