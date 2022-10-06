"""File with extra functions."""


def military_joke(num: int) -> str:
    """This function return military joke.
    Args:
    num: int - joke number requested by the user.
    Returns:
    str: str - answer.
    """
    with open('military_joke.txt', 'r') as anek:
        text = [line for line in anek]
    output = ''.join(text[num - 1])
    if "\n" in output:
        output = output.replace('\n', '')
    return output


def corona_joke(num: int) -> str:
    """This function return coronavirus joke.
    Args:
    num: int - joke number requested by the user.
    Returns:
    str: str - answer.
    """
    with open('corona_joke.txt', 'r') as anek:
        text = [line for line in anek]
    output = ''.join(text[num - 1])
    if "\n" in output:
        output = output.replace('\n', '')
    return output


def cats_joke(num: int) -> str:
    """This function return cats joke.
    Args:
    num: int - joke number requested by the user.
    Returns:
    str - answer.
    """
    with open('cats_joke.txt', 'r') as anek:
        text = [line for line in anek]
    output = ''.join(text[num - 1])
    if "\n" in output:
        output = output.replace('\n', '')
    return output
