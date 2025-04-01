"""Case definitions for text transformation."""

__all__ = [
    "Case",
    "SNAKE",
    "CONSTANT",
    "KEBAB",
    "CAMEL",
    "PASCAL",
    "LOWER",
    "UPPER",
    "TITLE",
    "SENTENCE",
]

from dataclasses import dataclass
from doctest import testmod
from typing import Callable, Final, Iterable

from textcase.boundary import (
    ACRONYM,
    DIGIT_LOWER,
    DIGIT_UPPER,
    HYPHEN,
    LOWER_DIGIT,
    LOWER_UPPER,
    SPACE,
    UNDERSCORE,
    UPPER_DIGIT,
    Boundary,
)
from textcase.pattern import camel, capital, lower, sentence, upper


@dataclass(frozen=True)
class Case:
    """Represents a text case format for transformation.

    Each case format defines how to split and transform text into a specific
    case style. The `Case` class includes boundaries for splitting words,
    a transformation pattern, and a delimiter for joining the words.

    Examples:
    >>> Case(boundaries=(SPACE,), pattern=capital, delimiter=" ").delimiter
    ' '
    """

    boundaries: Iterable[Boundary]
    """The boundaries used to split the text into words."""

    pattern: Callable[[Iterable[str]], Iterable[str]] = lambda words: words
    """A callable that defines how to transform the split words into the desired case format."""

    delimiter: str = ""
    """The string used to join the transformed words together."""


SNAKE: Final[Case] = Case(
    boundaries=(UNDERSCORE,),
    pattern=lower,
    delimiter="_",
)
"""Snake case strings are delimited by underscores `_` and are all lowercase."""

CONSTANT: Final[Case] = Case(
    boundaries=(UNDERSCORE,),
    pattern=upper,
    delimiter="_",
)
"""Constant case strings are delimited by underscores `_` and are all uppercase."""

KEBAB: Final[Case] = Case(
    boundaries=(HYPHEN,),
    pattern=lower,
    delimiter="-",
)
"""Kebab case strings are delimited by hyphens `-` and are all lowercase."""

CAMEL: Final[Case] = Case(
    boundaries=(
        LOWER_UPPER,
        ACRONYM,
        LOWER_DIGIT,
        UPPER_DIGIT,
        DIGIT_LOWER,
        DIGIT_UPPER,
    ),
    pattern=camel,
)
"""Camel case strings are lowercase, but for every word *except the first* the first letter is capitalized."""

PASCAL: Final[Case] = Case(
    boundaries=(
        LOWER_UPPER,
        ACRONYM,
        LOWER_DIGIT,
        UPPER_DIGIT,
        DIGIT_LOWER,
        DIGIT_UPPER,
    ),
    pattern=capital,
)
"""Pascal case strings are lowercase, but for every word the first letter is capitalized."""

LOWER: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=lower,
    delimiter=" ",
)
"""Lowercase strings are delimited by spaces and all characters are lowercase."""

UPPER: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=upper,
    delimiter=" ",
)
"""Uppercase strings are delimited by spaces and all characters are uppercase."""

TITLE: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=capital,
    delimiter=" ",
)
"""Title case strings are delimited by spaces. Only the leading character of each word is uppercase."""

SENTENCE: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=sentence,
    delimiter=" ",
)
"""Sentence case strings are delimited by spaces. Only the leading character of the first word is uppercase."""


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
