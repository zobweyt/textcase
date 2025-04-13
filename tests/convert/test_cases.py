from textcase import case, convert


def test_snake() -> None:
    assert convert("ronnie james dio", case.SNAKE) == "ronnie_james_dio"


def test_constant() -> None:
    assert convert("Ronnie_James_dio", case.CONSTANT) == "RONNIE_JAMES_DIO"


def test_kebab() -> None:
    assert convert("RONNIE_JAMES_DIO", case.KEBAB) == "ronnie-james-dio"


def test_middot() -> None:
    assert convert("ronnie james dio", case.MIDDOT) == "ronnie·james·dio"


def test_camel() -> None:
    assert convert("RONNIE-JAMES-DIO", case.CAMEL) == "ronnieJamesDio"


def test_pascal() -> None:
    assert convert("ronnie-james-dio", case.PASCAL) == "RonnieJamesDio"


def test_lower() -> None:
    assert convert("RONNIE JAMES DIO", case.LOWER) == "ronnie james dio"


def test_upper() -> None:
    assert convert("ronnie james dio", case.UPPER) == "RONNIE JAMES DIO"


def test_title() -> None:
    assert convert("ronnie-james-dio", case.TITLE) == "Ronnie James Dio"


def test_sentence() -> None:
    assert convert("ronnie james dio", case.SENTENCE) == "Ronnie james dio"
