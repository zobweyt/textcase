"""Text case conversion.

**Added in version:** [`0.1.0`](https://zobweyt.github.io/textcase/changelog/#010-2025-03-31)
"""

__all__ = [
    "ACRONYM",
    "Boundary",
    "camel",
    "Case",
    "constant",
    "DIGIT_LOWER",
    "DIGIT_UPPER",
    "HYPHEN",
    "INTERPUNCT",
    "kebab",
    "LOWER_DIGIT",
    "LOWER_UPPER",
    "lower",
    "middot",
    "pascal",
    "sentence",
    "snake",
    "SPACE",
    "title",
    "UNDERSCORE",
    "UPPER_DIGIT",
    "UPPER_LOWER",
    "upper",
]

from dataclasses import dataclass
from string import punctuation
from typing import Callable, Iterable


@dataclass(frozen=True)
class Boundary:
    """Represents a condition for splitting an identifier into words.

    Some boundaries, [`HYPHEN`][textcase.HYPHEN], [`UNDERSCORE`][textcase.UNDERSCORE], [`SPACE`][textcase.SPACE],
    and [`INTERPUNCT`][textcase.INTERPUNCT] consume the character they split on, whereas the other boundaries do not.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    match: Callable[[str], bool]
    """A function that determines if this boundary is present in the string.
    
    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    start: int = 0
    """Where the beginning of the boundary is.
    
    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    length: int = 0
    """The length of the boundary. This is the number of graphemes that are removed when splitting.
    
    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    @staticmethod
    def from_delimiter(delimiter: str) -> "Boundary":
        """Create a new boundary instance from a delimiter string.

        This helper method provides an easy way to create basic boundaries like [`UNDERSCORE`][textcase.UNDERSCORE],
        [`HYPHEN`][textcase.HYPHEN], [`SPACE`][textcase.SPACE], and [`INTERPUNCT`][textcase.INTERPUNCT].

        **Added in version:** [`0.3.0`](https://zobweyt.github.io/textcase/changelog/#030-2025-04-13)

        Args:
            delimiter: A string to be used as the delimiter for creating the boundary.

        Returns:
            A new boundary instance, configured to match the provided delimiter.

        Examples:
            >>> Boundary.from_delimiter("_").start
            0

            >>> Boundary.from_delimiter("_").length
            1
        """
        return Boundary(match=lambda text: text[:1] == delimiter, length=len(delimiter))


UNDERSCORE = Boundary.from_delimiter("_")
"""Splits on `#!py "_"`, consuming the character on segmentation.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

HYPHEN = Boundary.from_delimiter("-")
"""Splits on `#!py "-"`, consuming the character on segmentation.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

SPACE = Boundary.from_delimiter(" ")
"""Splits on `#!py " "`, consuming the character on segmentation.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

INTERPUNCT = Boundary.from_delimiter("·")
"""Splits on `#!py "·"`, consuming the character on segmentation.

**Added in version:** [`0.3.0`](https://zobweyt.github.io/textcase/changelog/#030-2025-04-13)
"""

LOWER_UPPER = Boundary(match=lambda s: s[:1].islower() and s[1:2].isupper(), start=1)
"""Splits where a lowercase letter is followed by an uppercase letter `#!py "aA"`.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

UPPER_LOWER = Boundary(match=lambda s: s[:1].isupper() and s[1:2].islower(), start=1)
"""Splits where an uppercase letter is followed by a lowercase letter `#!py "Aa"`.

This is seldom used and is **not** included in the default boundaries.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

ACRONYM = Boundary(match=lambda s: s[:1].isupper() and s[1:2].isupper() and s[2:3].islower(), start=1)
"""Acronyms are identified by two uppercase letters followed by a lowercase letter.

The word boundary is between the two uppercase letters. For example, `#!py "HTTPRequest"`
would have an acronym boundary identified at `#!py "PRe"` and split into `#!py "HTTP"` and `#!py "Request"`.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

LOWER_DIGIT = Boundary(match=lambda s: s[:1].islower() and s[1:2].isdigit(), start=1)
"""Splits where a lowercase letter is followed by a digit `#!py "a1"`.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

UPPER_DIGIT = Boundary(match=lambda s: s[:1].isupper() and s[1:2].isdigit(), start=1)
"""Splits where an uppercase letter is followed by a digit `#!py "A1"`.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

DIGIT_LOWER = Boundary(match=lambda s: s[:1].isdigit() and s[1:2].islower(), start=1)
"""Splits where digit is followed by a lowercase letter `#!py "1a"`.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

DIGIT_UPPER = Boundary(match=lambda s: s[:1].isdigit() and s[1:2].isupper(), start=1)
"""Splits where digit is followed by an uppercase letter `#!py "1A"`.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""


@dataclass(frozen=True)
class Case:
    """Represents a text case format for transformation.

    Each case format defines how to split and transform text into a specific
    case style. The [`Case`][textcase.Case] class includes boundaries for splitting words,
    a transformation pattern, and a delimiter for joining the words.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    delimiter: str = ""
    """The string used to join the transformed words together.
    
    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    transform: Callable[[Iterable[str]], Iterable[str]] = lambda words: words
    """A callable that defines how to transform the split words into the desired case format.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
    """

    def match(
        self,
        text: str,
        *,
        boundaries: Iterable[Boundary] = (
            UNDERSCORE,
            HYPHEN,
            SPACE,
            INTERPUNCT,
            LOWER_UPPER,
            LOWER_DIGIT,
            UPPER_DIGIT,
            DIGIT_LOWER,
            DIGIT_UPPER,
            ACRONYM,
        ),
        strip_punctuation: bool = True,
    ) -> bool:
        """Check if the given text matches the specified case format.

        This function compares the input text with its converted version based on the specified
        case format. It returns `True` if the text is already in the desired case format, and `False` otherwise.

        **Added in version:** [`0.4.0`](https://zobweyt.github.io/textcase/changelog/#040-2025-04-14)

        Args:
            text: The input string to be checked.
            boundaries: A collection of boundary instances that define the split conditions.
            strip_punctuation: Whether to remove punctuation during processing.

        Returns:
            `True` if the text matches the specified case format, `False` otherwise.
        """
        return self(text, boundaries=boundaries, strip_punctuation=strip_punctuation) == text

    def __call__(
        self,
        text: str,
        *,
        boundaries: Iterable[Boundary] = (
            UNDERSCORE,
            HYPHEN,
            SPACE,
            INTERPUNCT,
            LOWER_UPPER,
            LOWER_DIGIT,
            UPPER_DIGIT,
            DIGIT_LOWER,
            DIGIT_UPPER,
            ACRONYM,
        ),
        strip_punctuation: bool = True,
    ) -> str:
        """Convert the given text to the specified case format.

        **Added in version:** [`0.4.0`](https://zobweyt.github.io/textcase/changelog/#040-2025-04-14)

        Args:
            text: The input string to be converted.
            boundaries: A collection of boundary instances that define the split conditions.
            strip_punctuation: Whether to remove punctuation during processing.

        Returns:
            The input string converted to the specified case format.
        """
        words: list[str] = []
        text_length = len(text)
        last_boundary_end = 0

        for i in range(text_length):
            for boundary in boundaries:
                if boundary.match(text[i:]):
                    boundary_start = i + boundary.start
                    if last_boundary_end < boundary_start:
                        words.append(text[last_boundary_end:boundary_start])
                    last_boundary_end = boundary_start + boundary.length
                    break

        if last_boundary_end < text_length:
            words.append(text[last_boundary_end:])

        text = self.delimiter.join(self.transform(words))

        if strip_punctuation:
            text = text.translate(str.maketrans(dict.fromkeys(set(punctuation) - {self.delimiter})))

        return text


snake = Case(
    delimiter="_",
    transform=lambda words: map(str.lower, words),
)
"""Snake case strings are delimited by underscores `_` and are all lowercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

constant = Case(
    delimiter="_",
    transform=lambda words: map(str.upper, words),
)
"""Constant case strings are delimited by underscores `_` and are all uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

kebab = Case(
    delimiter="-",
    transform=lambda words: map(str.lower, words),
)
"""Kebab case strings are delimited by hyphens `-` and are all lowercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

middot = Case(
    delimiter="·",
    transform=lambda words: map(str.lower, words),
)
"""Middot case strings are delimited by interpuncts `·` and are all lowercase.

**Added in version:** [`0.3.0`](https://zobweyt.github.io/textcase/changelog/#030-2025-04-13)
"""

camel = Case(
    transform=lambda words: (word.lower() if i == 0 else word.capitalize() for i, word in enumerate(words)),
)
"""Camel case strings are lowercase, but for every word *except the first* the first letter is capitalized.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

pascal = Case(
    transform=lambda words: map(str.capitalize, words),
)
"""Pascal case strings are lowercase, but for every word the first letter is capitalized.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

lower = Case(
    delimiter=" ",
    transform=lambda words: map(str.lower, words),
)
"""Lowercase strings are delimited by spaces and all characters are lowercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

upper = Case(
    delimiter=" ",
    transform=lambda words: map(str.upper, words),
)
"""Uppercase strings are delimited by spaces and all characters are uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

title = Case(
    delimiter=" ",
    transform=lambda words: map(str.capitalize, words),
)
"""Title case strings are delimited by spaces. Only the leading character of each word is uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

sentence = Case(
    delimiter=" ",
    transform=lambda words: (word.capitalize() if i == 0 else word.lower() for i, word in enumerate(words)),
)
"""Sentence case strings are delimited by spaces. Only the leading character of the first word is uppercase.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""
