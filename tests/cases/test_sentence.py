from textcase import SPACE, Boundary, sentence


def test_sentence_all_cases() -> None:
    """Correctly converts strings in various text case styles to Sentence case."""
    assert sentence("json_decode_error") == "Json decode error"
    assert sentence("HTTP_ERROR") == "Http error"
    assert sentence("url-parse-error") == "Url parse error"
    assert sentence("socket·timeout·error") == "Socket timeout error"
    assert sentence("valueError") == "Value error"
    assert sentence("IndexError") == "Index error"
    assert sentence("key error") == "Key error"
    assert sentence("TYPE ERROR") == "Type error"
    assert sentence("Attribute Error") == "Attribute error"
    assert sentence("File not found error") == "File not found error"


def test_sentence_non_ascii() -> None:
    """Correctly converts non-ASCII characters to Sentence case."""
    assert sentence("ὈΔΥΣΣΕΎΣ") == "Ὀδυσσεύς"
    assert sentence("XΣXΣ baﬄe") == "Xσxς baﬄe"
    assert sentence("GranatÄpfel") == "Granat äpfel"
    assert sentence("ПЕРСПЕКТИВА24") == "Перспектива 24"


def test_sentence_acronym() -> None:
    """Correctly converts acronyms to Sentence case."""
    assert sentence("XMLHttpRequest") == "Xml http request"
    assert sentence("IOStream") == "Io stream"
    assert sentence("myJSONParser") == "My json parser"


def test_sentence_punctuation() -> None:
    """Correctly converts punctuation to Sentence case."""
    assert sentence("10,000Days") == "10000 days"
    assert sentence("Hello, world!") == "Hello world"
    assert sentence("Hello, world!", strip_punctuation=False) == "Hello, world!"
    assert sentence("ONE\nTWO\nTHREE") == "One\ntwo\nthree"
    assert sentence("__weird--var _name-") == "Weird var name"
    assert sentence("Lorem ipsum dolor sit amet.") == "Lorem ipsum dolor sit amet"


def test_sentence_kitchen_sink() -> None:
    """Correctly converts a variety of mixed text case styles to Sentence case."""
    assert sentence("MixedUP camelCase, with some Spaces") == "Mixed up camel case with some spaces"
    assert sentence("mixed_up_ snake_case with some _spaces") == "Mixed up snake case with some spaces"
    assert sentence("this-contains_ ALLKinds OfWord_Boundaries") == "This contains all kinds of word boundaries"
    assert sentence("FIELD_NAME11") == "Field name 11"
    assert sentence("99BOTTLES") == "99 bottles"
    assert sentence("FieldNamE11") == "Field nam e 11"
    assert sentence("abc123def456") == "Abc 123 def 456"
    assert sentence("abc123DEF456") == "Abc 123 def 456"
    assert sentence("abc123Def456") == "Abc 123 def 456"
    assert sentence("abc123DEf456") == "Abc 123 d ef 456"
    assert sentence("ABC123def456") == "Abc 123 def 456"
    assert sentence("ABC123DEF456") == "Abc 123 def 456"
    assert sentence("ABC123Def456") == "Abc 123 def 456"
    assert sentence("ABC123DEf456") == "Abc 123 d ef 456"
    assert sentence("ABC123dEEf456FOO") == "Abc 123 d e ef 456 foo"
    assert sentence("abcDEF") == "Abc def"
    assert sentence("ABcDE") == "A bc de"


def test_sentence_boundaries_empty() -> None:
    """Correctly converts strings to Sentence case with an empty boundaries list."""
    assert sentence("04-16 HTTP Cat", boundaries=[]) == "0416 http cat"
    assert sentence("04-16 HTTP Cat", boundaries=[], strip_punctuation=False) == "04-16 http cat"


def test_sentence_boundaries_space() -> None:
    """Correctly converts strings to Sentence case using space as the only boundary."""
    assert sentence("04-16 HTTP Cat", boundaries=[SPACE]) == "0416 http cat"
    assert sentence("04-16 HTTP Cat", boundaries=[SPACE], strip_punctuation=False) == "04-16 http cat"


def test_sentence_boundaries_custom() -> None:
    """Correctly converts strings to Sentence case using a custom boundary as the only boundary."""
    assert sentence("colors.brown", boundaries=[Boundary.from_delimiter(".")]) == "Colors brown"


def test_sentence_match_true() -> None:
    """Matches strings that are Sentence case."""
    assert sentence.match("File not found error") is True


def test_sentence_match_false() -> None:
    """Does not match strings that are Sentence case."""
    assert sentence.match("json_decode_error") is False
    assert sentence.match("HTTP_ERROR") is False
    assert sentence.match("url-parse-error") is False
    assert sentence.match("socket·timeout·error") is False
    assert sentence.match("valueError") is False
    assert sentence.match("IndexError") is False
    assert sentence.match("key error") is False
    assert sentence.match("TYPE ERROR") is False
    assert sentence.match("Attribute Error") is False
