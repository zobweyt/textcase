from textcase import SPACE, Boundary, constant


def test_constant_all_cases() -> None:
    """Correctly converts strings in various text case styles to CONSTANT_CASE."""
    assert constant("json_decode_error") == "JSON_DECODE_ERROR"
    assert constant("HTTP_ERROR") == "HTTP_ERROR"
    assert constant("url-parse-error") == "URL_PARSE_ERROR"
    assert constant("socket·timeout·error") == "SOCKET_TIMEOUT_ERROR"
    assert constant("valueError") == "VALUE_ERROR"
    assert constant("IndexError") == "INDEX_ERROR"
    assert constant("key error") == "KEY_ERROR"
    assert constant("TYPE ERROR") == "TYPE_ERROR"
    assert constant("Attribute Error") == "ATTRIBUTE_ERROR"
    assert constant("File not found error") == "FILE_NOT_FOUND_ERROR"


def test_constant_non_ascii() -> None:
    """Correctly converts non-ASCII characters to CONSTANT_CASE."""
    assert constant("ὈΔΥΣΣΕΎΣ") == "ὈΔΥΣΣΕΎΣ"
    assert constant("XΣXΣ baﬄe") == "XΣXΣ_BAFFLE"
    assert constant("GranatÄpfel") == "GRANAT_ÄPFEL"
    assert constant("ПЕРСПЕКТИВА24") == "ПЕРСПЕКТИВА_24"


def test_constant_acronym() -> None:
    """Correctly converts acronyms to CONSTANT_CASE."""
    assert constant("XMLHttpRequest") == "XML_HTTP_REQUEST"
    assert constant("IOStream") == "IO_STREAM"
    assert constant("myJSONParser") == "MY_JSON_PARSER"


def test_constant_punctuation() -> None:
    """Correctly converts punctuation to CONSTANT_CASE."""
    assert constant("10,000Days") == "10000_DAYS"
    assert constant("Hello, world!") == "HELLO_WORLD"
    assert constant("Hello, world!", strip_punctuation=False) == "HELLO,_WORLD!"
    assert constant("ONE\nTWO\nTHREE") == "ONE\nTWO\nTHREE"
    assert constant("__weird--var _name-") == "WEIRD_VAR_NAME"
    assert constant("Lorem ipsum dolor sit amet.") == "LOREM_IPSUM_DOLOR_SIT_AMET"


def test_constant_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to CONSTANT_CASE."""
    assert constant("MixedUP camelCase, with some Spaces") == "MIXED_UP_CAMEL_CASE_WITH_SOME_SPACES"
    assert constant("mixed_up_ snake_case with some _spaces") == "MIXED_UP_SNAKE_CASE_WITH_SOME_SPACES"
    assert constant("this-contains_ ALLKinds OfWord_Boundaries") == "THIS_CONTAINS_ALL_KINDS_OF_WORD_BOUNDARIES"
    assert constant("FIELD_NAME11") == "FIELD_NAME_11"
    assert constant("99BOTTLES") == "99_BOTTLES"
    assert constant("FieldNamE11") == "FIELD_NAM_E_11"
    assert constant("abc123def456") == "ABC_123_DEF_456"
    assert constant("abc123DEF456") == "ABC_123_DEF_456"
    assert constant("abc123Def456") == "ABC_123_DEF_456"
    assert constant("abc123DEf456") == "ABC_123_D_EF_456"
    assert constant("ABC123def456") == "ABC_123_DEF_456"
    assert constant("ABC123DEF456") == "ABC_123_DEF_456"
    assert constant("ABC123Def456") == "ABC_123_DEF_456"
    assert constant("ABC123DEf456") == "ABC_123_D_EF_456"
    assert constant("ABC123dEEf456FOO") == "ABC_123_D_E_EF_456_FOO"
    assert constant("abcDEF") == "ABC_DEF"
    assert constant("ABcDE") == "A_BC_DE"


def test_constant_boundaries_empty() -> None:
    """Correctly converts strings to CONSTANT_CASE with an empty boundaries list."""
    assert constant("04-16 HTTP Cat", boundaries=[]) == "0416 HTTP CAT"
    assert constant("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 HTTP CAT"


def test_constant_boundaries_space() -> None:
    """Correctly converts strings to CONSTANT_CASE using space as the only boundary."""
    assert constant("04-16 HTTP Cat", boundaries=[SPACE]) == "0416_HTTP_CAT"
    assert constant("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16_HTTP_CAT"


def test_constant_boundaries_custom() -> None:
    """Correctly converts strings to CONSTANT_CASE using a custom boundary as the only boundary."""
    assert constant("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "COLORS_BROWN"


def test_constant_match_true() -> None:
    """Matches strings that are CONSTANT_CASE."""
    assert constant.match("HTTP_ERROR") is True


def test_constant_match_false() -> None:
    """Does not match strings that are CONSTANT_CASE."""
    assert constant.match("json_decode_error") is False
    assert constant.match("url-parse-error") is False
    assert constant.match("socket·timeout·error") is False
    assert constant.match("valueError") is False
    assert constant.match("IndexError") is False
    assert constant.match("key error") is False
    assert constant.match("TYPE ERROR") is False
    assert constant.match("Attribute Error") is False
    assert constant.match("File not found error") is False
