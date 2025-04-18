from textcase import SPACE, Boundary, upper


def test_upper_all_cases() -> None:
    """Correctly converts strings in various text case styles to UPPER CASE."""
    assert upper("json_decode_error") == "JSON DECODE ERROR"
    assert upper("HTTP_ERROR") == "HTTP ERROR"
    assert upper("url-parse-error") == "URL PARSE ERROR"
    assert upper("socket·timeout·error") == "SOCKET TIMEOUT ERROR"
    assert upper("valueError") == "VALUE ERROR"
    assert upper("IndexError") == "INDEX ERROR"
    assert upper("key error") == "KEY ERROR"
    assert upper("TYPE ERROR") == "TYPE ERROR"
    assert upper("Attribute Error") == "ATTRIBUTE ERROR"
    assert upper("File not found error") == "FILE NOT FOUND ERROR"


def test_upper_non_ascii() -> None:
    """Correctly converts non-ASCII characters to UPPER CASE."""
    assert upper("ὈΔΥΣΣΕΎΣ") == "ὈΔΥΣΣΕΎΣ"
    assert upper("XΣXΣ baﬄe") == "XΣXΣ BAFFLE"
    assert upper("GranatÄpfel") == "GRANAT ÄPFEL"
    assert upper("ПЕРСПЕКТИВА24") == "ПЕРСПЕКТИВА 24"


def test_upper_acronym() -> None:
    """Correctly converts acronyms to UPPER CASE."""
    assert upper("XMLHttpRequest") == "XML HTTP REQUEST"
    assert upper("IOStream") == "IO STREAM"
    assert upper("myJSONParser") == "MY JSON PARSER"


def test_upper_punctuation() -> None:
    """Correctly converts punctuation to UPPER CASE."""
    assert upper("10,000Days") == "10000 DAYS"
    assert upper("Hello, world!") == "HELLO WORLD"
    assert upper("Hello, world!", strip_punctuation=False) == "HELLO, WORLD!"
    assert upper("ONE\nTWO\nTHREE") == "ONE\nTWO\nTHREE"
    assert upper("__weird--var _name-") == "WEIRD VAR NAME"
    assert upper("Lorem ipsum dolor sit amet.") == "LOREM IPSUM DOLOR SIT AMET"


def test_upper_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to UPPER CASE."""
    assert upper("MixedUP camelCase, with some Spaces") == "MIXED UP CAMEL CASE WITH SOME SPACES"
    assert upper("mixed_up_ snake_case with some _spaces") == "MIXED UP SNAKE CASE WITH SOME SPACES"
    assert upper("this-contains_ ALLKinds OfWord_Boundaries") == "THIS CONTAINS ALL KINDS OF WORD BOUNDARIES"
    assert upper("FIELD_NAME11") == "FIELD NAME 11"
    assert upper("99BOTTLES") == "99 BOTTLES"
    assert upper("FieldNamE11") == "FIELD NAM E 11"
    assert upper("abc123def456") == "ABC 123 DEF 456"
    assert upper("abc123DEF456") == "ABC 123 DEF 456"
    assert upper("abc123Def456") == "ABC 123 DEF 456"
    assert upper("abc123DEf456") == "ABC 123 D EF 456"
    assert upper("ABC123def456") == "ABC 123 DEF 456"
    assert upper("ABC123DEF456") == "ABC 123 DEF 456"
    assert upper("ABC123Def456") == "ABC 123 DEF 456"
    assert upper("ABC123DEf456") == "ABC 123 D EF 456"
    assert upper("ABC123dEEf456FOO") == "ABC 123 D E EF 456 FOO"
    assert upper("abcDEF") == "ABC DEF"
    assert upper("ABcDE") == "A BC DE"


def test_upper_boundaries_empty() -> None:
    """Correctly converts strings to UPPER CASE with an empty boundaries list."""
    assert upper("04-16 HTTP Cat", boundaries=[]) == "0416 HTTP CAT"
    assert upper("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 HTTP CAT"


def test_upper_boundaries_space() -> None:
    """Correctly converts strings to UPPER CASE using space as the only boundary."""
    assert upper("04-16 HTTP Cat", boundaries=[SPACE]) == "0416 HTTP CAT"
    assert upper("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16 HTTP CAT"


def test_upper_boundaries_custom() -> None:
    """Correctly converts strings to UPPER CASE using a custom boundary as the only boundary."""
    assert upper("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "COLORS BROWN"


def test_upper_match_true() -> None:
    """Matches strings that are UPPER CASE."""
    assert upper.match("TYPE ERROR") is True


def test_upper_match_false() -> None:
    """Does not match strings that are UPPER CASE."""
    assert upper.match("json_decode_error") is False
    assert upper.match("HTTP_ERROR") is False
    assert upper.match("url-parse-error") is False
    assert upper.match("socket·timeout·error") is False
    assert upper.match("valueError") is False
    assert upper.match("IndexError") is False
    assert upper.match("key error") is False
    assert upper.match("Attribute Error") is False
    assert upper.match("File not found error") is False
