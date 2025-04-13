"""Text case conversion.

**Added in version:** [`0.1.0`](https://zobweyt.github.io/textcase/changelog/#010-2025-03-31)

Examples:
    >>> convert("2020-04-16_my_cat_cali", case.SNAKE)
    '2020_04_16_my_cat_cali'

    >>> is_case("2020_04_16_my_cat_cali", case.SNAKE)
    True
"""

__all__ = [
    "boundary",
    "case",
    "CaseConverter",
    "is_case",
    "convert",
]

__version__ = "0.3.0"

from doctest import testmod
from typing import Iterable

from textcase import boundary, case
from textcase.converter import CaseConverter


def is_case(text: str, case: case.Case) -> bool:
    """Check if the given text matches the specified case format.

    This function compares the input text with its converted version based on the specified
    case format. It returns `True` if the text is already in the desired case format, and `False` otherwise.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        text: The input string to be checked.
        case: The case format to check against.

    Returns:
        `True` if the text matches the specified case format, `False` otherwise.

    Examples:
        >>> is_case("2020_04_16_my_cat_cali", case.SNAKE)
        True

        >>> is_case("2020-04-16-my-cat-cali", case.SNAKE)
        False
    """
    return text == convert(text, case)


def convert(text: str, case: case.Case, boundaries: Iterable[boundary.Boundary] = boundary.DEFAULT_BOUNDARIES) -> str:
    """Convert the given text to the specified case format.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        text: The input string to be converted.
        case: The case format to convert the text to.
        boundaries: A collection of Boundary instances that define the split conditions.

    Returns:
        The input string converted to the specified case format.

    Examples:
        >>> convert("2020-04-16_my_cat_cali", case.SNAKE)
        '2020_04_16_my_cat_cali'
    """
    return case.delimiter.join(case.pattern(boundary.split(text, boundaries)))


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
