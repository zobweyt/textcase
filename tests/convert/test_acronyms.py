from textcase import case, convert


def test_io_stream() -> None:
    assert convert("IOStream", case.SNAKE) == "io_stream"


def test_my_json_parser() -> None:
    assert convert("myJSONParser", case.SNAKE) == "my_json_parser"


def test_weird_var_name() -> None:
    assert convert("__weird--var _name-", case.SNAKE) == "weird_var_name"
