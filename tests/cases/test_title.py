from textcase import SPACE, Boundary, title


def test_title_all_cases() -> None:
    """Correctly converts strings in various text case styles to Title Case."""
    assert title("json_decode_error") == "Json Decode Error"
    assert title("HTTP_ERROR") == "Http Error"
    assert title("url-parse-error") == "Url Parse Error"
    assert title("socket·timeout·error") == "Socket Timeout Error"
    assert title("valueError") == "Value Error"
    assert title("IndexError") == "Index Error"
    assert title("key error") == "Key Error"
    assert title("TYPE ERROR") == "Type Error"
    assert title("Attribute Error") == "Attribute Error"
    assert title("File not found error") == "File Not Found Error"


def test_title_non_ascii() -> None:
    """Correctly converts non-ASCII characters to Title Case."""
    assert title("ὈΔΥΣΣΕΎΣ") == "Ὀδυσσεύς"
    assert title("XΣXΣ baﬄe") == "Xσxς Baﬄe"
    assert title("GranatÄpfel") == "Granat Äpfel"
    assert title("ПЕРСПЕКТИВА24") == "Перспектива 24"


def test_title_acronym() -> None:
    """Correctly converts acronyms to Title Case."""
    assert title("XMLHttpRequest") == "Xml Http Request"
    assert title("IOStream") == "Io Stream"
    assert title("myJSONParser") == "My Json Parser"


def test_title_punctuation() -> None:
    """Correctly converts punctuation to Title Case."""
    assert title("10,000Days") == "10000 Days"
    assert title("Hello, world!") == "Hello World"
    assert title("Hello, world!", strip_punctuation=False) == "Hello, World!"
    assert title("ONE\nTWO\nTHREE") == "One\ntwo\nthree"
    assert title("__weird--var _name-") == "Weird Var Name"
    assert title("Lorem ipsum dolor sit amet.") == "Lorem Ipsum Dolor Sit Amet"


def test_title_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to Title Case."""
    assert title("MixedUP camelCase, with some Spaces") == "Mixed Up Camel Case With Some Spaces"
    assert title("mixed_up_ snake_case with some _spaces") == "Mixed Up Snake Case With Some Spaces"
    assert title("this-contains_ ALLKinds OfWord_Boundaries") == "This Contains All Kinds Of Word Boundaries"
    assert title("FIELD_NAME11") == "Field Name 11"
    assert title("99BOTTLES") == "99 Bottles"
    assert title("FieldNamE11") == "Field Nam E 11"
    assert title("abc123def456") == "Abc 123 Def 456"
    assert title("abc123DEF456") == "Abc 123 Def 456"
    assert title("abc123Def456") == "Abc 123 Def 456"
    assert title("abc123DEf456") == "Abc 123 D Ef 456"
    assert title("ABC123def456") == "Abc 123 Def 456"
    assert title("ABC123DEF456") == "Abc 123 Def 456"
    assert title("ABC123Def456") == "Abc 123 Def 456"
    assert title("ABC123DEf456") == "Abc 123 D Ef 456"
    assert title("ABC123dEEf456FOO") == "Abc 123 D E Ef 456 Foo"
    assert title("abcDEF") == "Abc Def"
    assert title("ABcDE") == "A Bc De"


def test_title_boundaries_empty() -> None:
    """Correctly converts strings to Title Case with an empty boundaries list."""
    assert title("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert title("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_title_boundaries_space() -> None:
    """Correctly converts strings to Title Case using space as the only boundary."""
    assert title("04-16 HTTP Cat", boundaries=[SPACE]) == "0416 Http Cat"
    assert title("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16 Http Cat"


def test_title_boundaries_custom() -> None:
    """Correctly converts strings to Title Case using a custom boundary as the only boundary."""
    assert title("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "Colors Brown"


def test_title_match_true() -> None:
    """Matches strings that are Title Case."""
    assert title.match("Attribute Error") is True


def test_title_match_false() -> None:
    """Does not match strings that are Title Case."""
    assert title.match("json_decode_error") is False
    assert title.match("HTTP_ERROR") is False
    assert title.match("url-parse-error") is False
    assert title.match("socket·timeout·error") is False
    assert title.match("valueError") is False
    assert title.match("IndexError") is False
    assert title.match("key error") is False
    assert title.match("TYPE ERROR") is False
    assert title.match("File not found error") is False
