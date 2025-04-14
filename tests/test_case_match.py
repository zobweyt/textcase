import textcase


def test_snake() -> None:
    assert textcase.snake.match("ronnie_james_dio") is True
    assert textcase.snake.match("ronnie james dio") is False


def test_constant() -> None:
    assert textcase.constant.match("RONNIE_JAMES_DIO") is True
    assert textcase.constant.match("Ronnie_James_dio") is False


def test_kebab() -> None:
    assert textcase.kebab.match("ronnie-james-dio") is True
    assert textcase.kebab.match("RONNIE_JAMES_DIO") is False


def test_middot() -> None:
    assert textcase.middot.match("ronnie·james·dio") is True
    assert textcase.middot.match("RONNIE_JAMES_DIO") is False


def test_camel() -> None:
    assert textcase.camel.match("ronnieJamesDio") is True
    assert textcase.camel.match("RONNIE-JAMES-DIO") is False


def test_pascal() -> None:
    assert textcase.pascal.match("RonnieJamesDio") is True
    assert textcase.pascal.match("ronnie-james-dio") is False


def test_lower() -> None:
    assert textcase.lower.match("ronnie james dio") is True
    assert textcase.lower.match("RONNIE JAMES DIO") is False


def test_upper() -> None:
    assert textcase.upper.match("RONNIE JAMES DIO") is True
    assert textcase.upper.match("ronnie james dio") is False


def test_title() -> None:
    assert textcase.title.match("Ronnie James Dio") is True
    assert textcase.title.match("ronnie-james-dio") is False


def test_sentence() -> None:
    assert textcase.sentence.match("Ronnie james dio") is True
    assert textcase.sentence.match("ronnie james dio") is False
