import textcase


def test_boundaries() -> None:
    assert textcase.title("27-07_my_cat", boundaries=[textcase.UNDERSCORE], strip_punctuation=False) == "27-07 My Cat"
