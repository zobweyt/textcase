"""Text case conversion.

## Example

```python
import textcase

print(textcase.convert("2020-04-16_my_cat_cali", textcase.case.SNAKE))  # 2020_04_16_my_cat_cali
print(textcase.is_case("2020_04_16_my_cat_cali", textcase.case.SNAKE))  # True
```
"""

__all__ = [
    "boundary",
    "case",
    "CaseConverter",
    "is_case",
    "convert",
]

__version__ = "0.2.1"

from doctest import testmod
from typing import Iterable

from textcase import boundary, case
from textcase.converter import CaseConverter


def is_case(text: str, case: case.Case) -> bool:
    """Check if the given text matches the specified case format.

    This function compares the input text with its converted version based on the specified
    case format. It returns `True` if the text is already in the desired case format, and `False` otherwise.

    Args:
        text (str): The input string to be checked.
        case (case.Case): The case format to check against, which should be an instance of `case.Case`.

    Returns:
        `True` if the text matches the specified case format, `False` otherwise.

    Examples:
        >>> assert is_case("2020_04_16_my_cat_cali", case.SNAKE) == True
        >>> assert is_case("2020-04-16-my-cat-cali", case.SNAKE) == False
    """
    return text == convert(text, case)


def convert(text: str, case: case.Case, boundaries: Iterable[boundary.Boundary] = boundary.DEFAULT_BOUNDARIES) -> str:
    """Convert the given text to the specified case format.

    Args:
        text (str): The input string to be converted.
        case (case.Case): The case format to convert the text to, which should be an instance of `case.Case`.
        boundaries (Iterable[Boundary], optional): A collection of Boundary instances that define the split conditions.

    Returns:
        str: The input string converted to the specified case format.

    Examples:
        >>> assert convert("2020-04-16_my_cat_cali", case.SNAKE) == "2020_04_16_my_cat_cali"
        >>> assert convert("my_Cat-CALI", case.CAMEL) == "myCatCali"
    """
    return case.delimiter.join(case.pattern(boundary.split(text, boundaries)))


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
