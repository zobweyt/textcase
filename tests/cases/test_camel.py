from textcase import SPACE, Boundary, camel


def test_camel_all_cases() -> None:
    """Correctly converts strings in various text case styles to camelCase."""
    assert camel("json_decode_error") == "jsonDecodeError"
    assert camel("HTTP_ERROR") == "httpError"
    assert camel("url-parse-error") == "urlParseError"
    assert camel("socket·timeout·error") == "socketTimeoutError"
    assert camel("valueError") == "valueError"
    assert camel("IndexError") == "indexError"
    assert camel("key error") == "keyError"
    assert camel("TYPE ERROR") == "typeError"
    assert camel("Attribute Error") == "attributeError"
    assert camel("File not found error") == "fileNotFoundError"


def test_camel_non_ascii() -> None:
    """Correctly converts non-ASCII characters to camelCase."""
    assert camel("ὈΔΥΣΣΕΎΣ") == "ὀδυσσεύς"
    assert camel("XΣXΣ baﬄe") == "xσxςBaﬄe"
    assert camel("GranatÄpfel") == "granatÄpfel"
    assert camel("ПЕРСПЕКТИВА24") == "перспектива24"


def test_camel_acronym() -> None:
    """Correctly converts acronyms to camelCase."""
    assert camel("XMLHttpRequest") == "xmlHttpRequest"
    assert camel("IOStream") == "ioStream"
    assert camel("myJSONParser") == "myJsonParser"


def test_camel_punctuation() -> None:
    """Correctly converts punctuation to camelCase."""
    assert camel("10,000Days") == "10000Days"
    assert camel("Hello, world!") == "helloWorld"
    assert camel("Hello, world!", strip_punctuation=False) == "hello,World!"
    assert camel("ONE\nTWO\nTHREE") == "one\ntwo\nthree"
    assert camel("__weird--var _name-") == "weirdVarName"
    assert camel("Lorem ipsum dolor sit amet.") == "loremIpsumDolorSitAmet"


def test_camel_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to camelCase."""
    assert camel("MixedUP camelCase, with some Spaces") == "mixedUpCamelCaseWithSomeSpaces"
    assert camel("mixed_up_ snake_case with some _spaces") == "mixedUpSnakeCaseWithSomeSpaces"
    assert camel("this-contains_ ALLKinds OfWord_Boundaries") == "thisContainsAllKindsOfWordBoundaries"
    assert camel("FIELD_NAME11") == "fieldName11"
    assert camel("99BOTTLES") == "99Bottles"
    assert camel("FieldNamE11") == "fieldNamE11"
    assert camel("abc123def456") == "abc123Def456"
    assert camel("abc123DEF456") == "abc123Def456"
    assert camel("abc123Def456") == "abc123Def456"
    assert camel("abc123DEf456") == "abc123DEf456"
    assert camel("ABC123def456") == "abc123Def456"
    assert camel("ABC123DEF456") == "abc123Def456"
    assert camel("ABC123Def456") == "abc123Def456"
    assert camel("ABC123DEf456") == "abc123DEf456"
    assert camel("ABC123dEEf456FOO") == "abc123DEEf456Foo"
    assert camel("abcDEF") == "abcDef"
    assert camel("ABcDE") == "aBcDe"


def test_camel_boundaries_empty() -> None:
    """Correctly converts strings to camelCase with an empty boundaries list."""
    assert camel("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert camel("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_camel_boundaries_space() -> None:
    """Correctly converts strings to camelCase using space as the only boundary."""
    assert camel("04-16 HTTP Cat", boundaries=[SPACE]) == "0416HttpCat"
    assert camel("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16HttpCat"


def test_camel_boundaries_custom() -> None:
    """Correctly converts strings to camelCase using a custom boundary as the only boundary."""
    assert camel("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "colorsBrown"


def test_camel_match_true() -> None:
    """Matches strings that are camelCase."""
    assert camel.match("valueError") is True


def test_camel_match_false() -> None:
    """Does not match strings that are camelCase."""
    assert camel.match("json_decode_error") is False
    assert camel.match("HTTP_ERROR") is False
    assert camel.match("url-parse-error") is False
    assert camel.match("socket·timeout·error") is False
    assert camel.match("IndexError") is False
    assert camel.match("key error") is False
    assert camel.match("TYPE ERROR") is False
    assert camel.match("Attribute Error") is False
    assert camel.match("File not found error") is False
