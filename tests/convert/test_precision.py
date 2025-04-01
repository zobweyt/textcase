from textcase import boundary, case, convert


def test_boundaries() -> None:
    assert convert("2020-04-16_my_cat_cali", case.TITLE, (boundary.UNDERSCORE,)) == "2020-04-16 My Cat Cali"
