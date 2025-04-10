"""Text case transformation patterns.

**Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

Examples:
    >>> tuple(lower(("Hello", "World")))
    ('hello', 'world')

    >>> tuple(upper(("Hello", "World")))
    ('HELLO', 'WORLD')

    >>> tuple(capital(("hello", "world")))
    ('Hello', 'World')

    >>> tuple(camel(("hello", "world")))
    ('hello', 'World')

    >>> tuple(sentence(("hello", "world")))
    ('Hello', 'world')
"""

__all__ = [
    "lower",
    "upper",
    "capital",
    "camel",
    "sentence",
]

from doctest import testmod
from itertools import chain
from typing import Iterable, Iterator


def lower(words: Iterable[str]) -> Iterator[str]:
    """Convert all words to lowercase.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        words: An iterable of words to convert.

    Yields:
        An iterator of words in lowercase.

    Examples:
        >>> tuple(lower(("Hello", "World")))
        ('hello', 'world')
    """
    return (word.lower() for word in words)


def upper(words: Iterable[str]) -> Iterator[str]:
    """Convert all words to uppercase.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        words: An iterable of words to convert.

    Yields:
        An iterator of words in uppercase.

    Examples:
        >>> tuple(upper(("Hello", "World")))
        ('HELLO', 'WORLD')
    """
    return (word.upper() for word in words)


def capital(words: Iterable[str]) -> Iterator[str]:
    """Capitalize the first letter of each word and make the rest lowercase.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        words: An iterable of words to convert.

    Yields:
        An iterator of words with the first letter capitalized.

    Examples:
        >>> tuple(capital(("hello", "world")))
        ('Hello', 'World')
    """
    return (word.capitalize() for word in words)


def camel(words: Iterable[str]) -> Iterator[str]:
    """Convert the first word to lowercase and capitalize the remaining words.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        words: An iterable of words to convert.

    Yields:
        An iterator of words in camel case format.

    Examples:
        >>> tuple(camel(("hello", "world")))
        ('hello', 'World')
    """
    words_iter = iter(words)
    first_word = next(words_iter, "").lower()
    return chain((first_word,), (word.capitalize() for word in words_iter))


def sentence(words: Iterable[str]) -> Iterator[str]:
    """Capitalize the first word and make the remaining words lowercase.

    **Added in version:** [`0.2.0`](https://zobweyt.github.io/textcase/changelog/#020-2025-04-01)

    Args:
        words: An iterable of words to convert.

    Yields:
        An iterator of words in sentence case format.

    Examples:
        >>> tuple(sentence(("hello", "world")))
        ('Hello', 'world')
    """
    words_iter = iter(words)
    first_word = next(words_iter, "").capitalize()
    return chain((first_word,), (word.lower() for word in words_iter))


if __name__ == "__main__":
    testmod(verbose=True)  # pragma: no cover
