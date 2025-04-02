"""Conditions for splitting an identifier into words."""

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

    Some boundaries, `HYPHEN`, `UNDERSCORE`, and `SPACE`, consume the character theysplit on,
    whereas the other boundaries do not.

    ## Example:

    You can also create custom boundaries:

    ```python
    from textcase.boundary import Boundary

    UNDERSCORE = Boundary(
        satisfies=lambda text: text.startswith("_"),
        length=1,
    )
    ```
    """

    satisfies: Callable[[str], bool]
    """A function that determines if this boundary is present at the start of the string."""

    start: int = 0
    """Where the beginning of the boundary is."""

    length: int = 0
    """The length of the boundary. This is the number of graphemes that are removed when splitting."""


UNDERSCORE: Final[Boundary] = Boundary(
    satisfies=lambda text: text.startswith("_"),
    length=1,
)
"""
Splits on `_`, consuming the character on segmentation.
"""

HYPHEN: Final[Boundary] = Boundary(
    satisfies=lambda text: text.startswith("-"),
    length=1,
)
"""
Splits on `-`, consuming the character on segmentation.
"""

SPACE: Final[Boundary] = Boundary(
    satisfies=lambda text: text.startswith(" "),
    length=1,
)
"""
Splits on space, consuming the character on segmentation.
"""

LOWER_UPPER: Final[Boundary] = Boundary(
    satisfies=lambda text: len(text) > 1 and text[0].islower() and text[1].isupper(),
    start=1,
)
"""
Splits where a lowercase letter is followed by an uppercase letter.
"""

UPPER_LOWER: Final[Boundary] = Boundary(
    satisfies=lambda text: len(text) > 1 and text[0].isupper() and text[1].islower(),
    start=1,
)
"""
Splits where an uppercase letter is followed by a lowercase letter.
This is seldom used and is **not** included in the `DEFAULT_BOUNDARIES`.
"""

ACRONYM: Final[Boundary] = Boundary(
    satisfies=lambda text: len(text) > 2 and text[0].isupper() and text[1].isupper() and text[2].islower(),
    start=1,
)
"""
Acronyms are identified by two uppercase letters followed by a lowercase letter.
The word boundary is between the two uppercase letters.  For example, "HTTPRequest"
would have an acronym boundary identified at "PRe" and split into "HTTP" and "Request".
"""

LOWER_DIGIT: Final[Boundary] = Boundary(
    satisfies=lambda text: len(text) > 1 and text[0].islower() and text[1].isdigit(),
    start=1,
)
"""
Splits where a lowercase letter is followed by a digit.
"""

UPPER_DIGIT: Final[Boundary] = Boundary(
    satisfies=lambda text: len(text) > 1 and text[0].isupper() and text[1].isdigit(),
    start=1,
)
"""
Splits where an uppercase letter is followed by a digit.
"""

DIGIT_LOWER: Final[Boundary] = Boundary(
    satisfies=lambda text: len(text) > 1 and text[0].isdigit() and text[1].islower(),
    start=1,
)
"""
Splits where digit is followed by a lowercase letter.
"""

DIGIT_UPPER: Final[Boundary] = Boundary(
    satisfies=lambda text: len(text) > 1 and text[0].isdigit() and text[1].isupper(),
    start=1,
)
"""
Splits where digit is followed by an uppercase letter.
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
"""
Default boundaries used for splitting strings into words:

* underscores `_`
* hyphens `-`
* spaces ` `
* changes in capitalization from lowercase to uppercase `aA`
* adjacent digits and letters `a1`, `1a`, `A1`, `1A`
* acroynms `AAa` (as in `HTTPRequest`)
"""


def split(text: str, boundaries: Iterable[Boundary] = DEFAULT_BOUNDARIES) -> Iterator[str]:
    """Split an identifier into a list of words using the provided boundaries.

    This function iterates through the input text and splits it into words based on the
    specified boundary conditions. It yields each word found in the text, excluding
    empty strings.

    Args:
        text (str): The input string to be split into words.
        boundaries (Iterable[Boundary], optional): A collection of Boundary instances that define the split conditions.

    Yields:
        Iterator[str]: An iterator over the words extracted from the input text.

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
    that can split the text `into` multiple parts or that do not match the entire `text`.

    Args:
        text (str): The input string to be analyzed for boundaries.

    Yields:
        Iterator[Boundary]: An iterator over `Boundary` instances that are identified within the given `text`.

    Examples:
        >>> assert (HYPHEN, SPACE, LOWER_UPPER, UPPER_DIGIT, DIGIT_LOWER) == tuple(get_boundaries("aA8a -"))
        >>> assert (UNDERSCORE, LOWER_UPPER, DIGIT_UPPER, ACRONYM) == tuple(get_boundaries("bD:0B:_:AAa"))
    """

    for boundary in DEFAULT_BOUNDARIES:
        parts = tuple(split(text, [boundary]))

        if len(parts) > 1 or len(parts) == 0 or parts[0] != text:
            yield boundary


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
