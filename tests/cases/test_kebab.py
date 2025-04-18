from textcase import SPACE, Boundary, kebab


def test_kebab_all_cases() -> None:
    """Correctly converts strings in various text case styles to kebab-case."""
    assert kebab("json_decode_error") == "json-decode-error"
    assert kebab("HTTP_ERROR") == "http-error"
    assert kebab("url-parse-error") == "url-parse-error"
    assert kebab("socket·timeout·error") == "socket-timeout-error"
    assert kebab("valueError") == "value-error"
    assert kebab("IndexError") == "index-error"
    assert kebab("key error") == "key-error"
    assert kebab("TYPE ERROR") == "type-error"
    assert kebab("Attribute Error") == "attribute-error"
    assert kebab("File not found error") == "file-not-found-error"


def test_kebab_non_ascii() -> None:
    """Correctly converts non-ASCII characters to kebab-case."""
    assert kebab("ὈΔΥΣΣΕΎΣ") == "ὀδυσσεύς"
    assert kebab("XΣXΣ baﬄe") == "xσxς-baﬄe"
    assert kebab("GranatÄpfel") == "granat-äpfel"
    assert kebab("ПЕРСПЕКТИВА24") == "перспектива-24"


def test_kebab_acronym() -> None:
    """Correctly converts acronyms to kebab-case."""
    assert kebab("XMLHttpRequest") == "xml-http-request"
    assert kebab("IOStream") == "io-stream"
    assert kebab("myJSONParser") == "my-json-parser"


def test_kebab_punctuation() -> None:
    """Correctly converts punctuation to kebab-case."""
    assert kebab("10,000Days") == "10000-days"
    assert kebab("Hello, world!") == "hello-world"
    assert kebab("Hello, world!", strip_punctuation=False) == "hello,-world!"
    assert kebab("ONE\nTWO\nTHREE") == "one\ntwo\nthree"
    assert kebab("__weird--var _name-") == "weird-var-name"
    assert kebab("Lorem ipsum dolor sit amet.") == "lorem-ipsum-dolor-sit-amet"


def test_kebab_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to kebab-case."""
    assert kebab("MixedUP camelCase, with some Spaces") == "mixed-up-camel-case-with-some-spaces"
    assert kebab("mixed_up_ snake_case with some _spaces") == "mixed-up-snake-case-with-some-spaces"
    assert kebab("this-contains_ ALLKinds OfWord_Boundaries") == "this-contains-all-kinds-of-word-boundaries"
    assert kebab("FIELD_NAME11") == "field-name-11"
    assert kebab("99BOTTLES") == "99-bottles"
    assert kebab("FieldNamE11") == "field-nam-e-11"
    assert kebab("abc123def456") == "abc-123-def-456"
    assert kebab("abc123DEF456") == "abc-123-def-456"
    assert kebab("abc123Def456") == "abc-123-def-456"
    assert kebab("abc123DEf456") == "abc-123-d-ef-456"
    assert kebab("ABC123def456") == "abc-123-def-456"
    assert kebab("ABC123DEF456") == "abc-123-def-456"
    assert kebab("ABC123Def456") == "abc-123-def-456"
    assert kebab("ABC123DEf456") == "abc-123-d-ef-456"
    assert kebab("ABC123dEEf456FOO") == "abc-123-d-e-ef-456-foo"
    assert kebab("abcDEF") == "abc-def"
    assert kebab("ABcDE") == "a-bc-de"


def test_kebab_boundaries_empty() -> None:
    """Correctly converts strings to kebab-case with an empty boundaries list."""
    assert kebab("04-16 HTTP Cat", boundaries=[]) == "04-16 http cat"
    assert kebab("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_kebab_boundaries_space() -> None:
    """Correctly converts strings to kebab-case using space as the only boundary."""
    assert kebab("04-16 HTTP Cat", boundaries=[SPACE]) == "04-16-http-cat"
    assert kebab("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16-http-cat"


def test_kebab_boundaries_custom() -> None:
    """Correctly converts strings to kebab-case using a custom boundary as the only boundary."""
    assert kebab("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "colors-brown"


def test_kebab_match_true() -> None:
    """Matches strings that are kebab-case."""
    assert kebab.match("url-parse-error") is True


def test_kebab_match_false() -> None:
    """Does not match strings that are kebab-case."""
    assert kebab.match("json_decode_error") is False
    assert kebab.match("HTTP_ERROR") is False
    assert kebab.match("socket·timeout·error") is False
    assert kebab.match("valueError") is False
    assert kebab.match("IndexError") is False
    assert kebab.match("key error") is False
    assert kebab.match("TYPE ERROR") is False
    assert kebab.match("Attribute Error") is False
    assert kebab.match("File not found error") is False
