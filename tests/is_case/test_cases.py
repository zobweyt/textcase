from textcase import case, is_case


def test_snake() -> None:
    assert is_case("ronnie_james_dio", case.SNAKE) is True
    assert is_case("ronnie james dio", case.SNAKE) is False


def test_constant() -> None:
    assert is_case("RONNIE_JAMES_DIO", case.CONSTANT) is True
    assert is_case("Ronnie_James_dio", case.CONSTANT) is False


def test_kebab() -> None:
    assert is_case("ronnie-james-dio", case.KEBAB) is True
    assert is_case("RONNIE_JAMES_DIO", case.KEBAB) is False


def test_camel() -> None:
    assert is_case("ronnieJamesDio", case.CAMEL) is True
    assert is_case("RONNIE-JAMES-DIO", case.CAMEL) is False


def test_pascal() -> None:
    assert is_case("RonnieJamesDio", case.PASCAL) is True
    assert is_case("ronnie-james-dio", case.PASCAL) is False


def test_lower() -> None:
    assert is_case("ronnie james dio", case.LOWER) is True
    assert is_case("RONNIE JAMES DIO", case.LOWER) is False


def test_upper() -> None:
    assert is_case("RONNIE JAMES DIO", case.UPPER) is True
    assert is_case("ronnie james dio", case.UPPER) is False


def test_title() -> None:
    assert is_case("Ronnie James Dio", case.TITLE) is True
    assert is_case("ronnie-james-dio", case.TITLE) is False


def test_sentence() -> None:
    assert is_case("Ronnie james dio", case.SENTENCE) is True
    assert is_case("ronnie james dio", case.SENTENCE) is False
