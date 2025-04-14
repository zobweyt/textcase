import textcase


def test_boundaries() -> None:
    assert textcase.title("27-07 my cat", boundaries=[textcase.UNDERSCORE], strip_punctuation=False) == "27-07 my cat"
