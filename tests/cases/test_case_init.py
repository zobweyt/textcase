from textcase import SPACE, Boundary, Case

dot = Case(delimiter=".", transform=lambda words: map(str.lower, words))


def test_dot_all_cases() -> None:
    """Correctly converts strings in various text case styles to dot.case."""
    assert dot("json_decode_error") == "json.decode.error"
    assert dot("HTTP_ERROR") == "http.error"
    assert dot("url-parse-error") == "url.parse.error"
    assert dot("socket·timeout·error") == "socket.timeout.error"
    assert dot("valueError") == "value.error"
    assert dot("IndexError") == "index.error"
    assert dot("key error") == "key.error"
    assert dot("TYPE ERROR") == "type.error"
    assert dot("Attribute Error") == "attribute.error"
    assert dot("File not found error") == "file.not.found.error"


def test_dot_non_ascii() -> None:
    """Correctly converts non-ASCII characters to dot.case."""
    assert dot("ὈΔΥΣΣΕΎΣ") == "ὀδυσσεύς"
    assert dot("XΣXΣ baﬄe") == "xσxς.baﬄe"
    assert dot("GranatÄpfel") == "granat.äpfel"
    assert dot("ПЕРСПЕКТИВА24") == "перспектива.24"


def test_dot_acronym() -> None:
    """Correctly converts acronyms to dot.case."""
    assert dot("XMLHttpRequest") == "xml.http.request"
    assert dot("IOStream") == "io.stream"
    assert dot("myJSONParser") == "my.json.parser"


def test_dot_punctuation() -> None:
    """Correctly converts punctuation to dot.case."""
    assert dot("10,000Days") == "10000.days"
    assert dot("Hello, world!") == "hello.world"
    assert dot("Hello, world!", strip_punctuation=False) == "hello,.world!"
    assert dot("ONE\nTWO\nTHREE") == "one\ntwo\nthree"
    assert dot("__weird--var _name-") == "weird.var.name"
    assert dot("Lorem ipsum dolor sit amet.") == "lorem.ipsum.dolor.sit.amet"


def test_dot_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to dot.case."""
    assert dot("MixedUP camelCase, with some Spaces") == "mixed.up.camel.case.with.some.spaces"
    assert dot("mixed_up_ snake_case with some _spaces") == "mixed.up.snake.case.with.some.spaces"
    assert dot("this-contains_ ALLKinds OfWord_Boundaries") == "this.contains.all.kinds.of.word.boundaries"
    assert dot("FIELD_NAME11") == "field.name.11"
    assert dot("99BOTTLES") == "99.bottles"
    assert dot("FieldNamE11") == "field.nam.e.11"
    assert dot("abc123def456") == "abc.123.def.456"
    assert dot("abc123DEF456") == "abc.123.def.456"
    assert dot("abc123Def456") == "abc.123.def.456"
    assert dot("abc123DEf456") == "abc.123.d.ef.456"
    assert dot("ABC123def456") == "abc.123.def.456"
    assert dot("ABC123DEF456") == "abc.123.def.456"
    assert dot("ABC123Def456") == "abc.123.def.456"
    assert dot("ABC123DEf456") == "abc.123.d.ef.456"
    assert dot("ABC123dEEf456FOO") == "abc.123.d.e.ef.456.foo"
    assert dot("abcDEF") == "abc.def"
    assert dot("ABcDE") == "a.bc.de"


def test_dot_boundaries_empty() -> None:
    """Correctly converts strings to dot.case with an empty boundaries list."""
    assert dot("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert dot("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_dot_boundaries_space() -> None:
    """Correctly converts strings to dot.case using space as the only boundary."""
    assert dot("04-16 HTTP Cat", boundaries=[SPACE]) == "0416.http.cat"
    assert dot("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16.http.cat"


def test_dot_boundaries_custom() -> None:
    """Correctly converts strings to dot.case using a custom boundary as the only boundary."""
    assert dot("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "colors.brown"


def test_dot_match_true() -> None:
    """Matches strings that are dot.case."""
    assert dot.match("colors.brown") is True


def test_dot_match_false() -> None:
    """Does not match strings that are dot.case."""
    assert dot.match("json_decode_error") is False
    assert dot.match("HTTP_ERROR") is False
    assert dot.match("url-parse-error") is False
    assert dot.match("socket·timeout·error") is False
    assert dot.match("valueError") is False
    assert dot.match("IndexError") is False
    assert dot.match("key error") is False
    assert dot.match("TYPE ERROR") is False
    assert dot.match("Attribute Error") is False
    assert dot.match("File not found error") is False
