from textcase import SPACE, Boundary, snake


def test_snake_all_cases() -> None:
    """Correctly converts strings in various text case styles to snake_case."""
    assert snake("json_decode_error") == "json_decode_error"
    assert snake("HTTP_ERROR") == "http_error"
    assert snake("url-parse-error") == "url_parse_error"
    assert snake("socket·timeout·error") == "socket_timeout_error"
    assert snake("valueError") == "value_error"
    assert snake("IndexError") == "index_error"
    assert snake("key error") == "key_error"
    assert snake("TYPE ERROR") == "type_error"
    assert snake("Attribute Error") == "attribute_error"
    assert snake("File not found error") == "file_not_found_error"


def test_snake_non_ascii() -> None:
    """Correctly converts non-ASCII characters to snake_case."""
    assert snake("ὈΔΥΣΣΕΎΣ") == "ὀδυσσεύς"
    assert snake("XΣXΣ baﬄe") == "xσxς_baﬄe"
    assert snake("GranatÄpfel") == "granat_äpfel"
    assert snake("ПЕРСПЕКТИВА24") == "перспектива_24"


def test_snake_acronym() -> None:
    """Correctly converts acronyms to snake_case."""
    assert snake("XMLHttpRequest") == "xml_http_request"
    assert snake("IOStream") == "io_stream"
    assert snake("myJSONParser") == "my_json_parser"


def test_snake_punctuation() -> None:
    """Correctly converts punctuation to snake_case."""
    assert snake("10,000Days") == "10000_days"
    assert snake("Hello, world!") == "hello_world"
    assert snake("Hello, world!", strip_punctuation=False) == "hello,_world!"
    assert snake("ONE\nTWO\nTHREE") == "one\ntwo\nthree"
    assert snake("__weird--var _name-") == "weird_var_name"
    assert snake("Lorem ipsum dolor sit amet.") == "lorem_ipsum_dolor_sit_amet"


def test_snake_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to snake_case."""
    assert snake("MixedUP camelCase, with some Spaces") == "mixed_up_camel_case_with_some_spaces"
    assert snake("mixed_up_ snake_case with some _spaces") == "mixed_up_snake_case_with_some_spaces"
    assert snake("this-contains_ ALLKinds OfWord_Boundaries") == "this_contains_all_kinds_of_word_boundaries"
    assert snake("FIELD_NAME11") == "field_name_11"
    assert snake("99BOTTLES") == "99_bottles"
    assert snake("FieldNamE11") == "field_nam_e_11"
    assert snake("abc123def456") == "abc_123_def_456"
    assert snake("abc123DEF456") == "abc_123_def_456"
    assert snake("abc123Def456") == "abc_123_def_456"
    assert snake("abc123DEf456") == "abc_123_d_ef_456"
    assert snake("ABC123def456") == "abc_123_def_456"
    assert snake("ABC123DEF456") == "abc_123_def_456"
    assert snake("ABC123Def456") == "abc_123_def_456"
    assert snake("ABC123DEf456") == "abc_123_d_ef_456"
    assert snake("ABC123dEEf456FOO") == "abc_123_d_e_ef_456_foo"
    assert snake("abcDEF") == "abc_def"
    assert snake("ABcDE") == "a_bc_de"


def test_snake_boundaries_empty() -> None:
    """Correctly converts strings to snake_case with an empty boundaries list."""
    assert snake("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert snake("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_snake_boundaries_space() -> None:
    """Correctly converts strings to snake_case using space as the only boundary."""
    assert snake("04-16 HTTP Cat", boundaries=[SPACE]) == "0416_http_cat"
    assert snake("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16_http_cat"


def test_snake_boundaries_custom() -> None:
    """Correctly converts strings to snake_case using a custom boundary as the only boundary."""
    assert snake("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "colors_brown"


def test_snake_match_true() -> None:
    """Matches strings that are snake_case."""
    assert snake.match("json_decode_error") is True


def test_snake_match_false() -> None:
    """Does not match strings that are snake_case."""
    assert snake.match("HTTP_ERROR") is False
    assert snake.match("url-parse-error") is False
    assert snake.match("socket·timeout·error") is False
    assert snake.match("valueError") is False
    assert snake.match("IndexError") is False
    assert snake.match("key error") is False
    assert snake.match("TYPE ERROR") is False
    assert snake.match("Attribute Error") is False
    assert snake.match("File not found error") is False
