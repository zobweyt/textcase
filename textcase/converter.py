"""Text case conversion between different case formats.

## Examples:

```python
from textcase import CaseConverter, case

converter = CaseConverter()
converter.to_case(case.SNAKE)
converter.convert("myCatCali")  # "my_cat_cali"
converter.to_case(case.CAMEL)
converter.convert("my_cat_cali")  # "myCatCali"
```
"""

__all__ = [
    "CaseConverter",
]

from doctest import testmod
from typing import Callable, Iterable, List

from textcase.boundary import DEFAULT_BOUNDARIES, Boundary, split
from textcase.case import Case


class CaseConverter:
    """Represents a utility class for converting text between different case formats.

    ## Examples:

    ```python
    from textcase import CaseConverter, case

    converter = CaseConverter()
    converter.to_case(case.SNAKE)
    converter.convert("myCatCali")  # "my_cat_cali"
    converter.to_case(case.CAMEL)
    converter.convert("my_cat_cali")  # "myCatCali"
    ```
    """

    boundaries: list[Boundary]
    """A list of boundary conditions used for splitting text into words."""

    pattern: Callable[[Iterable[str]], Iterable[str]]
    """A callable that defines how to transform the split words into the desired case format."""

    delimiter: str
    """The string used to join the transformed words together."""

    def __init__(self) -> None:
        """Initializes a new `CaseConverter` instance with default boundaries and an identity pattern."""
        self.boundaries = list(DEFAULT_BOUNDARIES)
        self.pattern = lambda words: words
        self.delimiter = ""

    def convert(self, text: str) -> str:
        """Convert the given text to the specified case format.

        Args:
            text (str): The input string to be converted.

        Returns:
            str: The input string converted to the specified case format.

        Examples:
            >>> import textcase; CaseConverter().to_case(textcase.case.SNAKE).convert("myCatCali")
            'my_cat_cali'
        """
        return self.delimiter.join(self.pattern(self.split(text)))

    def split(self, text: str) -> List[str]:
        """Split the input text into words based on the defined boundaries.

        Args:
            text (str): The input string to be split into words.

        Returns:
            List[str]: A list of words extracted from the input text.

        Examples:
            >>> CaseConverter().split("my_cat_cali")
            ['my', 'cat', 'cali']
        """
        return list(split(text, self.boundaries))

    def to_case(self, case: Case) -> "CaseConverter":
        """Set the case format to convert to.

        Args:
            case (Case): The case format to convert the text to, which should be an instance of `Case`.

        Returns:
            CaseConverter: The current instance of CaseConverter for method chaining.
        """
        self.pattern = case.pattern
        self.delimiter = case.delimiter
        return self

    def from_case(self, case: Case) -> "CaseConverter":
        """Set the boundaries based on the specified case format.

        Args:
            case (Case): The case format to derive boundaries from, which should be an instance of `Case`.

        Returns:
            CaseConverter: The current instance of CaseConverter for method chaining.
        """
        self.boundaries = list(case.boundaries)
        return self


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
