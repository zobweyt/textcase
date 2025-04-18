from textcase import SPACE, Boundary, middot


def test_middot_all_cases() -> None:
    """Correctly converts strings in various text case styles to middot·case."""
    assert middot("json_decode_error") == "json·decode·error"
    assert middot("HTTP_ERROR") == "http·error"
    assert middot("url-parse-error") == "url·parse·error"
    assert middot("socket·timeout·error") == "socket·timeout·error"
    assert middot("valueError") == "value·error"
    assert middot("IndexError") == "index·error"
    assert middot("key error") == "key·error"
    assert middot("TYPE ERROR") == "type·error"
    assert middot("Attribute Error") == "attribute·error"
    assert middot("File not found error") == "file·not·found·error"


def test_middot_non_ascii() -> None:
    """Correctly converts non-ASCII characters to middot·case."""
    assert middot("ὈΔΥΣΣΕΎΣ") == "ὀδυσσεύς"
    assert middot("XΣXΣ baﬄe") == "xσxς·baﬄe"
    assert middot("GranatÄpfel") == "granat·äpfel"
    assert middot("ПЕРСПЕКТИВА24") == "перспектива·24"


def test_middot_acronym() -> None:
    """Correctly converts acronyms to middot·case."""
    assert middot("XMLHttpRequest") == "xml·http·request"
    assert middot("IOStream") == "io·stream"
    assert middot("myJSONParser") == "my·json·parser"


def test_middot_punctuation() -> None:
    """Correctly converts punctuation to middot·case."""
    assert middot("10,000Days") == "10000·days"
    assert middot("Hello, world!") == "hello·world"
    assert middot("Hello, world!", strip_punctuation=False) == "hello,·world!"
    assert middot("ONE\nTWO\nTHREE") == "one\ntwo\nthree"
    assert middot("__weird--var _name-") == "weird·var·name"
    assert middot("Lorem ipsum dolor sit amet.") == "lorem·ipsum·dolor·sit·amet"


def test_middot_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to middot·case."""
    assert middot("MixedUP camelCase, with some Spaces") == "mixed·up·camel·case·with·some·spaces"
    assert middot("mixed_up_ snake_case with some _spaces") == "mixed·up·snake·case·with·some·spaces"
    assert middot("this-contains_ ALLKinds OfWord_Boundaries") == "this·contains·all·kinds·of·word·boundaries"
    assert middot("FIELD_NAME11") == "field·name·11"
    assert middot("99BOTTLES") == "99·bottles"
    assert middot("FieldNamE11") == "field·nam·e·11"
    assert middot("abc123def456") == "abc·123·def·456"
    assert middot("abc123DEF456") == "abc·123·def·456"
    assert middot("abc123Def456") == "abc·123·def·456"
    assert middot("abc123DEf456") == "abc·123·d·ef·456"
    assert middot("ABC123def456") == "abc·123·def·456"
    assert middot("ABC123DEF456") == "abc·123·def·456"
    assert middot("ABC123Def456") == "abc·123·def·456"
    assert middot("ABC123DEf456") == "abc·123·d·ef·456"
    assert middot("ABC123dEEf456FOO") == "abc·123·d·e·ef·456·foo"
    assert middot("abcDEF") == "abc·def"
    assert middot("ABcDE") == "a·bc·de"


def test_middot_boundaries_empty() -> None:
    """Correctly converts strings to middot·case with an empty boundaries list."""
    assert middot("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert middot("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_middot_boundaries_space() -> None:
    """Correctly converts strings to middot·case using space as the only boundary."""
    assert middot("04-16 HTTP Cat", boundaries=[SPACE]) == "0416·http·cat"
    assert middot("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16·http·cat"


def test_middot_boundaries_custom() -> None:
    """Correctly converts strings to middot·case using a custom boundary as the only boundary."""
    assert middot("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "colors·brown"


def test_middot_match_true() -> None:
    """Matches strings that are middot·case."""
    assert middot.match("socket·timeout·error") is True


def test_middot_match_false() -> None:
    """Does not match strings that are middot·case."""
    assert middot.match("json_decode_error") is False
    assert middot.match("url-parse-error") is False
    assert middot.match("url-parse-error") is False
    assert middot.match("valueError") is False
    assert middot.match("IndexError") is False
    assert middot.match("key error") is False
    assert middot.match("TYPE ERROR") is False
    assert middot.match("Attribute Error") is False
    assert middot.match("File not found error") is False
