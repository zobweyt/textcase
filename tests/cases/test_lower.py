from textcase import SPACE, Boundary, lower


def test_lower_all_cases() -> None:
    """Correctly converts strings in various text case styles to lower case."""
    assert lower("json_decode_error") == "json decode error"
    assert lower("HTTP_ERROR") == "http error"
    assert lower("url-parse-error") == "url parse error"
    assert lower("socket·timeout·error") == "socket timeout error"
    assert lower("valueError") == "value error"
    assert lower("IndexError") == "index error"
    assert lower("key error") == "key error"
    assert lower("TYPE ERROR") == "type error"
    assert lower("Attribute Error") == "attribute error"
    assert lower("File not found error") == "file not found error"


def test_lower_non_ascii() -> None:
    """Correctly converts non-ASCII characters to lower case."""
    assert lower("ὈΔΥΣΣΕΎΣ") == "ὀδυσσεύς"
    assert lower("XΣXΣ baﬄe") == "xσxς baﬄe"
    assert lower("GranatÄpfel") == "granat äpfel"
    assert lower("ПЕРСПЕКТИВА24") == "перспектива 24"


def test_lower_acronym() -> None:
    """Correctly converts acronyms to lower case."""
    assert lower("XMLHttpRequest") == "xml http request"
    assert lower("IOStream") == "io stream"
    assert lower("myJSONParser") == "my json parser"


def test_lower_punctuation() -> None:
    """Correctly converts punctuation to lower case."""
    assert lower("10,000Days") == "10000 days"
    assert lower("Hello, world!") == "hello world"
    assert lower("Hello, world!", strip_punctuation=False) == "hello, world!"
    assert lower("ONE\nTWO\nTHREE") == "one\ntwo\nthree"
    assert lower("__weird--var _name-") == "weird var name"
    assert lower("Lorem ipsum dolor sit amet.") == "lorem ipsum dolor sit amet"


def test_lower_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to lower case."""
    assert lower("MixedUP camelCase, with some Spaces") == "mixed up camel case with some spaces"
    assert lower("mixed_up_ snake_case with some _spaces") == "mixed up snake case with some spaces"
    assert lower("this-contains_ ALLKinds OfWord_Boundaries") == "this contains all kinds of word boundaries"
    assert lower("FIELD_NAME11") == "field name 11"
    assert lower("99BOTTLES") == "99 bottles"
    assert lower("FieldNamE11") == "field nam e 11"
    assert lower("abc123def456") == "abc 123 def 456"
    assert lower("abc123DEF456") == "abc 123 def 456"
    assert lower("abc123Def456") == "abc 123 def 456"
    assert lower("abc123DEf456") == "abc 123 d ef 456"
    assert lower("ABC123def456") == "abc 123 def 456"
    assert lower("ABC123DEF456") == "abc 123 def 456"
    assert lower("ABC123Def456") == "abc 123 def 456"
    assert lower("ABC123DEf456") == "abc 123 d ef 456"
    assert lower("ABC123dEEf456FOO") == "abc 123 d e ef 456 foo"
    assert lower("abcDEF") == "abc def"
    assert lower("ABcDE") == "a bc de"


def test_lower_boundaries_empty() -> None:
    """Correctly converts strings to lower case with an empty boundaries list."""
    assert lower("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert lower("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_lower_boundaries_space() -> None:
    """Correctly converts strings to lower case using space as the only boundary."""
    assert lower("04-16 HTTP Cat", boundaries=[SPACE]) == "0416 http cat"
    assert lower("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16 http cat"


def test_lower_boundaries_custom() -> None:
    """Correctly converts strings to lower case using a custom boundary as the only boundary."""
    assert lower("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "colors brown"


def test_lower_match_true() -> None:
    """Matches strings that are lower case."""
    assert lower.match("key error") is True


def test_lower_match_false() -> None:
    """Does not match strings that are lower case."""
    assert lower.match("json_decode_error") is False
    assert lower.match("HTTP_ERROR") is False
    assert lower.match("url-parse-error") is False
    assert lower.match("socket·timeout·error") is False
    assert lower.match("valueError") is False
    assert lower.match("IndexError") is False
    assert lower.match("TYPE ERROR") is False
    assert lower.match("Attribute Error") is False
    assert lower.match("File not found error") is False
