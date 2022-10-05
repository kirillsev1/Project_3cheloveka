"""File with extra functions."""


def military_joke(numb: int) -> str:
    """This function return military joke.

    Args:
        numb: int - joke number requested by the user.

    Returns:
        str: str - answer.
    """
    text = []
    file = open('military_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[numb-1])
    if "\n" in output:
        output = output.replace('\n', '')
    file.close()
    return output


def corona_joke(numb: int) -> str:
    """"This function return coronavirus joke.

    Args:
        numb: int - joke number requested by the user.

    Returns:
        str: str - answer.
    """
    text = []
    file = open('corona_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[numb-1])
    if "\n" in output:
        output = output.replace('\n', '')
    file.close()
    return output


def cats_joke(numb: int) -> str:
    """"This function return cats joke.

    Args:
        numb: int - joke number requested by the user.

    Returns:
        str - answer.
    """
    text = []
    file = open('cats.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[numb-1])
    if "\n" in output:
        output = output.replace('\n', '')
    file.close()
    return output
