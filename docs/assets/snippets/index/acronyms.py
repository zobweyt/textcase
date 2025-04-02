from textcase import case, convert

print(convert("IOStream", case.SNAKE))  # io_stream
print(convert("myJSONParser", case.SNAKE))  # my_json_parser
print(convert("__weird--var _name-", case.SNAKE))  # weird_var_name
