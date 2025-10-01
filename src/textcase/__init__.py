"""Text case conversion."""

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
from typing import Callable, Iterable, TypeVar

_TBoundary = TypeVar("_TBoundary", bound="Boundary")


@dataclass(frozen=True)
class Boundary:
    """Represents a condition for splitting an identifier into words.

    Some boundaries, `HYPHEN`, `UNDERSCORE`, `SPACE`, and `INTERPUNCT` consume
    the character they split on, whereas the other boundaries do not.

    Examples:

        >>> DOT = Boundary(match=lambda text: text[:1] == ".", length=1)

        >>> DOT.match(".brown")
        True

        >>> DOT.match("_brown")
        False

        >>> DOT.start
        0

        >>> DOT.length
        1
    """

    match: Callable[[str], bool]
    """A function that determines if this boundary is present in the string."""

    start: int = 0
    """Where the beginning of the boundary is."""

    length: int = 0
    """The length of the boundary. This is the number of graphemes that are removed when splitting."""

    @classmethod
    def from_delimiter(cls: type[_TBoundary], delimiter: str) -> _TBoundary:
        """Create a new boundary instance from a delimiter string.

        This method makes it easier to create basic boundaries like `UNDERSCORE`, `HYPHEN`, `SPACE`, and `INTERPUNCT`.

        Args:
            delimiter: A string to be used as the delimiter for creating the boundary.

        Returns:
            A new boundary instance, configured to match the provided delimiter.

        Examples:

            >>> DOT = Boundary.from_delimiter(".")

            >>> DOT.match(".brown")
            True

            >>> DOT.match("_brown")
            False

            >>> DOT.start
            0

            >>> DOT.length
            1
        """
        return cls(match=lambda s: s.startswith(delimiter), length=len(delimiter))


UNDERSCORE = Boundary.from_delimiter("_")
"""Splits on underscore, consuming the character on segmentation.

Examples:

    >>> UNDERSCORE.match("_")
    True

    >>> UNDERSCORE.match("_brown")
    True

    >>> UNDERSCORE.match(".brown")
    False

    >>> UNDERSCORE.start
    0

    >>> UNDERSCORE.length
    1
"""

HYPHEN = Boundary.from_delimiter("-")
"""Splits on hyphen, consuming the character on segmentation.

Examples:

    >>> HYPHEN.match("-")
    True

    >>> HYPHEN.match("-brown")
    True

    >>> HYPHEN.match(".brown")
    False

    >>> HYPHEN.start
    0

    >>> HYPHEN.length
    1
"""

SPACE = Boundary.from_delimiter(" ")
"""Splits on space, consuming the character on segmentation.

Examples:

    >>> SPACE.match(" ")
    True

    >>> SPACE.match(" brown")
    True

    >>> SPACE.match(".brown")
    False

    >>> SPACE.start
    0

    >>> SPACE.length
    1
"""

INTERPUNCT = Boundary.from_delimiter("·")
"""Splits on interpunct, consuming the character on segmentation.

Examples:

    >>> INTERPUNCT.match("·")
    True

    >>> INTERPUNCT.match("·brown")
    True

    >>> INTERPUNCT.match(".brown")
    False

    >>> INTERPUNCT.start
    0

    >>> INTERPUNCT.length
    1
"""

LOWER_UPPER = Boundary(match=lambda s: s[:1].islower() and s[1:2].isupper(), start=1)
"""Splits where a lowercase letter is followed by an uppercase letter.

This is seldom used, and is not included in the default boundaries.

Examples:

    >>> LOWER_UPPER.match("aA")
    True

    >>> LOWER_UPPER.match("Aa")
    False

    >>> LOWER_UPPER.start
    1

    >>> LOWER_UPPER.length
    0
"""

UPPER_LOWER = Boundary(match=lambda s: s[:1].isupper() and s[1:2].islower(), start=1)
"""Splits where an uppercase letter is followed by a lowercase letter.

Examples:

    >>> UPPER_LOWER.match("Aa")
    True

    >>> UPPER_LOWER.match("aA")
    False

    >>> UPPER_LOWER.start
    1

    >>> UPPER_LOWER.length
    0
"""

ACRONYM = Boundary(match=lambda s: s[:1].isupper() and s[1:2].isupper() and s[2:3].islower(), start=1)
"""Acronyms are identified by two uppercase letters followed by a lowercase letter.

The word boundary is between the two uppercase letters. For example, "HTTPRequest"
would have an acronym boundary identified at "PRe" and split into "HTTP" and "Request".

Examples:

    >>> ACRONYM.match("AAa")
    True

    >>> ACRONYM.match("1Aa")
    False

    >>> ACRONYM.match("AAA")
    False

    >>> ACRONYM.start
    1

    >>> ACRONYM.length
    0
"""

LOWER_DIGIT = Boundary(match=lambda s: s[:1].islower() and s[1:2].isdigit(), start=1)
"""Splits where a lowercase letter is followed by a digit.

Examples:

    >>> LOWER_DIGIT.match("a1")
    True

    >>> LOWER_DIGIT.match("1a")
    False

    >>> LOWER_DIGIT.start
    1

    >>> LOWER_DIGIT.length
    0
"""

UPPER_DIGIT = Boundary(match=lambda s: s[:1].isupper() and s[1:2].isdigit(), start=1)
"""Splits where an uppercase letter is followed by a digit.

Examples:

    >>> UPPER_DIGIT.match("A1")
    True

    >>> UPPER_DIGIT.match("1A")
    False

    >>> UPPER_DIGIT.start
    1

    >>> UPPER_DIGIT.length
    0
"""

DIGIT_LOWER = Boundary(match=lambda s: s[:1].isdigit() and s[1:2].islower(), start=1)
"""Splits where digit is followed by a lowercase letter.

Examples:

    >>> DIGIT_LOWER.match("1a")
    True

    >>> DIGIT_LOWER.match("1A")
    False

    >>> DIGIT_LOWER.start
    1

    >>> DIGIT_LOWER.length
    0
"""

DIGIT_UPPER = Boundary(match=lambda s: s[:1].isdigit() and s[1:2].isupper(), start=1)
"""Splits where digit is followed by an uppercase letter.

Examples:

    >>> DIGIT_UPPER.match("1A")
    True

    >>> DIGIT_UPPER.match("1a")
    False

    >>> DIGIT_UPPER.start
    1

    >>> DIGIT_UPPER.length
    0
"""


@dataclass(frozen=True)
class Case:
    """Represents a text case style.

    Each case instance defines how to split and transform text into a specific case style.

    Examples:

        >>> dot = Case(delimiter=".", transform=lambda words: map(str.lower, words))

        >>> dot("Dot case var")
        'dot.case.var'

        >>> dot.match("dot.case.var")
        True

        >>> dot.match("Dot case var")
        False

        >>> dot.delimiter
        '.'

    """

    delimiter: str = ""
    """The string used to join the transformed words together."""

    transform: Callable[[Iterable[str]], Iterable[str]] = lambda words: words
    """A callable that defines how to transform the split words into the desired case format."""

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
        """Check if the given string matches the specified text case style.

        This method compares the input string with its converted version.

        Args:
            text: The input string to be checked.
            boundaries: The boundaries that define how to split the given string.
            strip_punctuation: Whether to remove punctuation during conversion.

        Returns:
            `True` if the given string matches the specified text case style, and `False` otherwise.
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
        """Convert the given string to the specified case format.

        Args:
            text: The input string to be converted.
            boundaries: The boundaries that define how to split the given string.
            strip_punctuation: Whether to remove punctuation during conversion.

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
            text = text.strip(self.delimiter).translate(str.maketrans("", "", punctuation.replace(self.delimiter, "")))

        return text


snake = Case(
    delimiter="_",
    transform=lambda words: map(str.lower, words),
)
"""Snake case strings are delimited by underscores and are all lowercase.

Examples:

    >>> snake("Hello, world!")
    'hello_world'

    >>> snake.match("hello_world")
    True

    >>> snake.match("Hello, world!")
    False
"""

constant = Case(
    delimiter="_",
    transform=lambda words: map(str.upper, words),
)
"""Constant case strings are delimited by underscores and are all uppercase.

Examples:

    >>> constant("Hello, world!")
    'HELLO_WORLD'

    >>> constant.match("HELLO_WORLD")
    True

    >>> constant.match("Hello, world!")
    False
"""

kebab = Case(
    delimiter="-",
    transform=lambda words: map(str.lower, words),
)
"""Kebab case strings are delimited by hyphens and are all lowercase.

Examples:

    >>> kebab("Hello, world!")
    'hello-world'

    >>> kebab.match("hello-world")
    True

    >>> kebab.match("Hello, world!")
    False
"""

middot = Case(
    delimiter="·",
    transform=lambda words: map(str.lower, words),
)
"""Middot case strings are delimited by interpuncts and are all lowercase.

Examples:

    >>> middot("Hello, world!")
    'hello·world'

    >>> middot.match("hello·world")
    True

    >>> middot.match("Hello, world!")
    False
"""

camel = Case(
    transform=lambda words: (word.lower() if i == 0 else word.capitalize() for i, word in enumerate(words)),
)
"""Camel case strings are lowercase, but for every word *except the first* the first letter is capitalized.

Examples:

    >>> camel("Hello, world!")
    'helloWorld'

    >>> camel.match("helloWorld")
    True

    >>> camel.match("Hello, world!")
    False
"""

pascal = Case(
    transform=lambda words: map(str.capitalize, words),
)
"""Pascal case strings are lowercase, but for every word the first letter is capitalized.

Examples:

    >>> pascal("Hello, world!")
    'HelloWorld'

    >>> pascal.match("HelloWorld")
    True

    >>> pascal.match("Hello, world!")
    False
"""

lower = Case(
    delimiter=" ",
    transform=lambda words: map(str.lower, words),
)
"""Lowercase strings are delimited by spaces and all characters are lowercase.

Examples:

    >>> lower("Hello, world!")
    'hello world'

    >>> lower.match("hello world")
    True

    >>> lower.match("Hello, world!")
    False
"""

upper = Case(
    delimiter=" ",
    transform=lambda words: map(str.upper, words),
)
"""Uppercase strings are delimited by spaces and all characters are uppercase.

Examples:

    >>> upper("Hello, world!")
    'HELLO WORLD'

    >>> upper.match("HELLO WORLD")
    True

    >>> upper.match("Hello, world!")
    False
"""

title = Case(
    delimiter=" ",
    transform=lambda words: map(str.capitalize, words),
)
"""Title case strings are delimited by spaces. Only the leading character of each word is uppercase.

No inferences are made about language, so words like "as", "to", and "for" will still be capitalized.

Examples:

    >>> title("Hello, world!")
    'Hello World'
    
    >>> title.match("Hello World")
    True

    >>> title.match("Hello, world!")
    False
"""

sentence = Case(
    delimiter=" ",
    transform=lambda words: (word.capitalize() if i == 0 else word.lower() for i, word in enumerate(words)),
)
"""Sentence case strings are delimited by spaces. Only the leading character of the first word is uppercase.

Examples:

    >>> sentence("Hello, world!")
    'Hello world'

    >>> sentence.match("Hello world")
    True

    >>> sentence.match("Hello, world!")
    False
"""
