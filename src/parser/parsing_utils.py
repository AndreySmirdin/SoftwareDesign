def find_unescaped_symbols(user_input, interesting_symbols):
    in_single_quotes = False
    in_double_quotes = False
    result = []
    for (index, char) in enumerate(user_input):
        if not in_double_quotes and char == '\'':
            in_single_quotes ^= 1
        elif char == '\"':
            in_double_quotes ^= 1
        elif not in_single_quotes and char in interesting_symbols:
            result.append(index)

    return result


def find_symbols_not_in_quotes(data, character):
    in_single_quotes = False
    in_double_quotes = False
    result = []
    for (index, char) in enumerate(data):
        if not in_double_quotes and char == '\'':
            in_single_quotes ^= 1
        elif not in_single_quotes and char == '\"':
            in_double_quotes ^= 1
        elif not in_single_quotes and not in_double_quotes and char == character:
            result.append(index)
    return result
