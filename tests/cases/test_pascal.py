from textcase import SPACE, Boundary, pascal


def test_pascal_all_cases() -> None:
    """Correctly converts strings in various text case styles to PascalCase."""
    assert pascal("json_decode_error") == "JsonDecodeError"
    assert pascal("HTTP_ERROR") == "HttpError"
    assert pascal("url-parse-error") == "UrlParseError"
    assert pascal("socket·timeout·error") == "SocketTimeoutError"
    assert pascal("valueError") == "ValueError"
    assert pascal("IndexError") == "IndexError"
    assert pascal("key error") == "KeyError"
    assert pascal("TYPE ERROR") == "TypeError"
    assert pascal("Attribute Error") == "AttributeError"
    assert pascal("File not found error") == "FileNotFoundError"


def test_pascal_non_ascii() -> None:
    """Correctly converts non-ASCII characters to PascalCase."""
    assert pascal("ὈΔΥΣΣΕΎΣ") == "Ὀδυσσεύς"
    assert pascal("XΣXΣ baﬄe") == "XσxςBaﬄe"
    assert pascal("GranatÄpfel") == "GranatÄpfel"
    assert pascal("ПЕРСПЕКТИВА24") == "Перспектива24"


def test_pascal_acronym() -> None:
    """Correctly converts acronyms to PascalCase."""
    assert pascal("XMLHttpRequest") == "XmlHttpRequest"
    assert pascal("IOStream") == "IoStream"
    assert pascal("myJSONParser") == "MyJsonParser"


def test_pascal_punctuation() -> None:
    """Correctly converts punctuation to PascalCase."""
    assert pascal("10,000Days") == "10000Days"
    assert pascal("Hello, world!") == "HelloWorld"
    assert pascal("Hello, world!", strip_punctuation=False) == "Hello,World!"
    assert pascal("ONE\nTWO\nTHREE") == "One\ntwo\nthree"
    assert pascal("__weird--var _name-") == "WeirdVarName"
    assert pascal("Lorem ipsum dolor sit amet.") == "LoremIpsumDolorSitAmet"


def test_pascal_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to PascalCase."""
    assert pascal("MixedUP camelCase, with some Spaces") == "MixedUpCamelCaseWithSomeSpaces"
    assert pascal("mixed_up_ snake_case with some _spaces") == "MixedUpSnakeCaseWithSomeSpaces"
    assert pascal("this-contains_ ALLKinds OfWord_Boundaries") == "ThisContainsAllKindsOfWordBoundaries"
    assert pascal("FIELD_NAME11") == "FieldName11"
    assert pascal("99BOTTLES") == "99Bottles"
    assert pascal("FieldNamE11") == "FieldNamE11"
    assert pascal("abc123def456") == "Abc123Def456"
    assert pascal("abc123DEF456") == "Abc123Def456"
    assert pascal("abc123Def456") == "Abc123Def456"
    assert pascal("abc123DEf456") == "Abc123DEf456"
    assert pascal("ABC123def456") == "Abc123Def456"
    assert pascal("ABC123DEF456") == "Abc123Def456"
    assert pascal("ABC123Def456") == "Abc123Def456"
    assert pascal("ABC123DEf456") == "Abc123DEf456"
    assert pascal("ABC123dEEf456FOO") == "Abc123DEEf456Foo"
    assert pascal("abcDEF") == "AbcDef"
    assert pascal("ABcDE") == "ABcDe"


def test_pascal_boundaries_empty() -> None:
    """Correctly converts strings to PascalCase with an empty boundaries list."""
    assert pascal("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert pascal("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_pascal_boundaries_space() -> None:
    """Correctly converts strings to PascalCase using space as the only boundary."""
    assert pascal("04-16 HTTP Cat", boundaries=[SPACE]) == "0416HttpCat"
    assert pascal("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16HttpCat"


def test_pascal_boundaries_custom() -> None:
    """Correctly converts strings to PascalCase using a custom boundary as the only boundary."""
    assert pascal("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "ColorsBrown"


def test_pascal_match_true() -> None:
    """Matches strings that are PascalCase."""
    assert pascal.match("IndexError") is True


def test_pascal_match_false() -> None:
    """Does not match strings that are PascalCase."""
    assert pascal.match("json_decode_error") is False
    assert pascal.match("HTTP_ERROR") is False
    assert pascal.match("url-parse-error") is False
    assert pascal.match("socket·timeout·error") is False
    assert pascal.match("valueError") is False
    assert pascal.match("key error") is False
    assert pascal.match("TYPE ERROR") is False
    assert pascal.match("Attribute Error") is False
    assert pascal.match("File not found error") is False
