"""Case definitions for text transformation.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

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
    case style. The [`Case`][textcase.case.Case] class includes boundaries for splitting words,
    a transformation pattern, and a delimiter for joining the words.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Examples:
        >>> Case(boundaries=(SPACE,), pattern=capital, delimiter=" ").delimiter
        ' '
    """

    boundaries: Iterable[Boundary]
    """The boundaries used to split the text into words.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    pattern: Callable[[Iterable[str]], Iterable[str]] = lambda words: words
    """A callable that defines how to transform the split words into the desired case format.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    delimiter: str = ""
    """The string used to join the transformed words together.
    
    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """


SNAKE: Final[Case] = Case(
    boundaries=(UNDERSCORE,),
    pattern=lower,
    delimiter="_",
)
"""Snake case strings are delimited by underscores `_` and are all lowercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

CONSTANT: Final[Case] = Case(
    boundaries=(UNDERSCORE,),
    pattern=upper,
    delimiter="_",
)
"""Constant case strings are delimited by underscores `_` and are all uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

KEBAB: Final[Case] = Case(
    boundaries=(HYPHEN,),
    pattern=lower,
    delimiter="-",
)
"""Kebab case strings are delimited by hyphens `-` and are all lowercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

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
"""Camel case strings are lowercase, but for every word *except the first* the first letter is capitalized.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

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
"""Pascal case strings are lowercase, but for every word the first letter is capitalized.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

LOWER: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=lower,
    delimiter=" ",
)
"""Lowercase strings are delimited by spaces and all characters are lowercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

UPPER: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=upper,
    delimiter=" ",
)
"""Uppercase strings are delimited by spaces and all characters are uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

TITLE: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=capital,
    delimiter=" ",
)
"""Title case strings are delimited by spaces. Only the leading character of each word is uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

SENTENCE: Final[Case] = Case(
    boundaries=(SPACE,),
    pattern=sentence,
    delimiter=" ",
)
"""Sentence case strings are delimited by spaces. Only the leading character of the first word is uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
