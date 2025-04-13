"""Conditions for splitting an identifier into words.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

__all__ = [
    "Boundary",
    "UNDERSCORE",
    "HYPHEN",
    "SPACE",
    "LOWER_UPPER",
    "UPPER_LOWER",
    "ACRONYM",
    "LOWER_DIGIT",
    "UPPER_DIGIT",
    "DIGIT_LOWER",
    "DIGIT_UPPER",
    "DEFAULT_BOUNDARIES",
    "split",
    "get_boundaries",
]

from dataclasses import dataclass
from doctest import testmod
from typing import Callable, Final, Iterable, Iterator, Tuple


@dataclass(frozen=True)
class Boundary:
    """Represents a condition for splitting an identifier into words.

    Some boundaries, [`HYPHEN`][textcase.boundary.HYPHEN], [`UNDERSCORE`][textcase.boundary.UNDERSCORE],
    and [`SPACE`][textcase.boundary.SPACE], consume the character they split on, whereas the other boundaries do not.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Examples:
        ```python
        from textcase.boundary import Boundary

        UNDERSCORE = Boundary(
            satisfies=lambda text: text.startswith("_"),
            length=1,
        )
        ```
    """

    satisfies: Callable[[str], bool]
    """A function that determines if this boundary is present at the start of the string.
    
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


UNDERSCORE: Final[Boundary] = Boundary(
    satisfies=lambda text: text[:1] == "_",
    length=1,
)
"""Splits on `_`, consuming the character on segmentation.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

HYPHEN: Final[Boundary] = Boundary(
    satisfies=lambda text: text[:1] == "-",
    length=1,
)
"""Splits on `-`, consuming the character on segmentation.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

SPACE: Final[Boundary] = Boundary(
    satisfies=lambda text: text[:1] == " ",
    length=1,
)
"""Splits on space, consuming the character on segmentation.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

LOWER_UPPER: Final[Boundary] = Boundary(
    satisfies=lambda text: text[0:1].islower() and text[1:2].isupper(),
    start=1,
)
"""Splits where a lowercase letter is followed by an uppercase letter.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

UPPER_LOWER: Final[Boundary] = Boundary(
    satisfies=lambda text: text[0:1].isupper() and text[1:2].islower(),
    start=1,
)
"""Splits where an uppercase letter is followed by a lowercase letter.

This is seldom used and is **not** included in the [`DEFAULT_BOUNDARIES`][textcase.boundary.DEFAULT_BOUNDARIES].

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

ACRONYM: Final[Boundary] = Boundary(
    satisfies=lambda text: text[0:2].isalpha() and text[0:2].isupper() and text[2:3].islower(),
    start=1,
)
"""Acronyms are identified by two uppercase letters followed by a lowercase letter.

The word boundary is between the two uppercase letters. For example, "HTTPRequest"
would have an acronym boundary identified at "PRe" and split into "HTTP" and "Request".

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

LOWER_DIGIT: Final[Boundary] = Boundary(
    satisfies=lambda text: text[0:1].islower() and text[1:2].isdigit(),
    start=1,
)
"""Splits where a lowercase letter is followed by a digit.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

UPPER_DIGIT: Final[Boundary] = Boundary(
    satisfies=lambda text: text[0:1].isupper() and text[1:2].isdigit(),
    start=1,
)
"""Splits where an uppercase letter is followed by a digit.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

DIGIT_LOWER: Final[Boundary] = Boundary(
    satisfies=lambda text: text[0:1].isdigit() and text[1:2].islower(),
    start=1,
)
"""Splits where digit is followed by a lowercase letter.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

DIGIT_UPPER: Final[Boundary] = Boundary(
    satisfies=lambda text: text[0:1].isdigit() and text[1:2].isupper(),
    start=1,
)
"""Splits where digit is followed by an uppercase letter.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""

DEFAULT_BOUNDARIES: Final[Tuple[Boundary, ...]] = (
    UNDERSCORE,
    HYPHEN,
    SPACE,
    LOWER_UPPER,
    LOWER_DIGIT,
    UPPER_DIGIT,
    DIGIT_LOWER,
    DIGIT_UPPER,
    ACRONYM,
)
"""Default boundaries used for splitting strings into words.

* Underscores: `_`,
* Hyphens: `-`,
* Spaces: ` `,
* Changes in capitalization from lowercase to uppercase: `aA`,
* Adjacent digits and letters: `a1`, `1a`, `A1`, `1A`,
* Acronyms: `AAa` (as in `HTTPRequest`).

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)
"""


def split(text: str, boundaries: Iterable[Boundary] = DEFAULT_BOUNDARIES) -> Iterator[str]:
    """Split an identifier into a list of words using the provided boundaries.

    This function iterates through the input text and splits it into words based on the
    specified boundary conditions. It yields each word found in the text, excluding
    empty strings.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        text: The input string to be split into words.
        boundaries: A collection of Boundary instances that define the split conditions.

    Yields:
        An iterator over the words extracted from the input text.

    Examples:
        >>> assert ("one", "two", "three.four") == tuple(split("one_two-three.four", (UNDERSCORE, HYPHEN)))
    """
    if not text:
        return

    last_boundary_end = 0
    text_length = len(text)

    for i in range(text_length):
        for boundary in boundaries:
            if boundary.satisfies(text[i:]):
                boundary_byte_start = i + boundary.start
                boundary_byte_end = boundary_byte_start + boundary.length
                if last_boundary_end < boundary_byte_start:
                    yield text[last_boundary_end:boundary_byte_start]
                last_boundary_end = boundary_byte_end
                break

    if last_boundary_end < text_length:
        yield text[last_boundary_end:]


def get_boundaries(text: str) -> Iterator[Boundary]:
    """Identifies boundaries present in the given `text`.

    This function checks the provided `text` against the default boundaries and returns
    those that are present. It evaluates each boundary condition and yields the boundaries
    that can split the `text` into multiple parts or that do not match the entire `text`.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        text: The input string to be analyzed for boundaries.

    Yields:
        An iterator over [`Boundary`][textcase.boundary.Boundary] instances that are identified within the given `text`.

    Examples:
        >>> assert (HYPHEN, SPACE, LOWER_UPPER, UPPER_DIGIT, DIGIT_LOWER) == tuple(get_boundaries("aA8a -"))
        >>> assert (UNDERSCORE, LOWER_UPPER, DIGIT_UPPER, ACRONYM) == tuple(get_boundaries("bD:0B:_:AAa"))
    """

    for boundary in DEFAULT_BOUNDARIES:
        parts = tuple(split(text, (boundary,)))

        if len(parts) > 1 or len(parts) == 0 or parts[0] != text:
            yield boundary


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
