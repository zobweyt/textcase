import textcase


def test_snake() -> None:
    assert textcase.snake("ronnie james dio") == "ronnie_james_dio"


def test_constant() -> None:
    assert textcase.constant("Ronnie_James_dio") == "RONNIE_JAMES_DIO"


def test_kebab() -> None:
    assert textcase.kebab("RONNIE_JAMES_DIO") == "ronnie-james-dio"


def test_middot() -> None:
    assert textcase.middot("ronnie james dio") == "ronnie·james·dio"


def test_camel() -> None:
    assert textcase.camel("RONNIE-JAMES-DIO") == "ronnieJamesDio"


def test_pascal() -> None:
    assert textcase.pascal("ronnie-james-dio") == "RonnieJamesDio"


def test_lower() -> None:
    assert textcase.lower("RONNIE JAMES DIO") == "ronnie james dio"


def test_upper() -> None:
    assert textcase.upper("ronnie james dio") == "RONNIE JAMES DIO"


def test_title() -> None:
    assert textcase.title("ronnie-james-dio") == "Ronnie James Dio"


def test_sentence() -> None:
    assert textcase.sentence("ronnie james dio") == "Ronnie james dio"
