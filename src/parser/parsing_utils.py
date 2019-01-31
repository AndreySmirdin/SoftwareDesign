def find_unescaped_symbols(user_input, interesting_symbols):
    """
    Find characters that have special meaning.
    :param user_input: input
    :param interesting_symbols: list of characters that we want to check
    :return: indices of unescaped characters
    """
    in_single_quotes = False
    in_double_quotes = False
    result = []
    for (index, char) in enumerate(user_input):
        in_single_quotes, in_double_quotes = _change_state(in_single_quotes, in_double_quotes, char)
        if not in_single_quotes and char in interesting_symbols:
            result.append(index)

    return result


def find_symbols_not_in_quotes(data, characters):
    """
    Finding characters that are not in quotes.
    :param data: input
    :param characters: list of characters that we want to check
    :return: indices of characters that are not in quotes
    """
    in_single_quotes = False
    in_double_quotes = False
    result = []
    for (index, char) in enumerate(data):
        if not in_single_quotes and not in_double_quotes and char in characters:
            result.append(index)
        in_single_quotes, in_double_quotes = _change_state(in_single_quotes, in_double_quotes, char)
        if not in_single_quotes and not in_double_quotes and char in characters and index not in result:
            result.append(index)
    return result


def check_quotes_correctness(data):
    """
    Check if all quotes are closed.
    :return: True if the string is valid.
    """
    in_single_quotes = False
    in_double_quotes = False
    for char in data:
        in_single_quotes, in_double_quotes = _change_state(in_single_quotes, in_double_quotes, char)

    return not (in_single_quotes or in_double_quotes)


def remove_quotes(commands):
    """
    Removing unescaped quotes for all words.
    :param commands: list of commands each of them is a list of arguments
    :return: Commands without quotes
    """
    result = []
    for command in commands:
        result.append([])
        for word in command:
            to_be_removed = find_symbols_not_in_quotes(word, ['\'', '\"'])
            new_word = ""
            for (index, c) in enumerate(word):
                if index not in to_be_removed:
                    new_word += c
            result[-1].append(new_word)
    return result


def _change_state(in_single, in_double, char):
    if not in_double and char == '\'':
        in_single ^= 1
    elif not in_single and char == '\"':
        in_double ^= 1
    return in_single, in_double
