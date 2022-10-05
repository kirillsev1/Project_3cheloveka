"""File with extra functions."""


def military_joke(n: int) -> str:
    """This function return military joke.
    Args:
        n: int - joke number requested by the user.
    Returns:
        str: str - answer.
    """
    text = []
    file = open('military_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[n-1])
    if "\n" in output:
        output = output.replace('\n', '')
    file.close()
    return output


def corona_joke(n: int) -> str:
    """"This function return coronavirus joke.
    Args:
        n: int - joke number requested by the user.
    Returns:
        str: str - answer.
    """
    text = []
    file = open('corona_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[n-1])
    if "\n" in output:
        output = output.replace('\n', '')
    file.close()
    return output


def cats_joke(n: int) -> str:
    """"This function return cats joke.
    Args:
        n: int - joke number requested by the user.
    Returns:
        str - answer.
    """
    text = []
    file = open('cats_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[n-1])
    if "\n" in output:
        output = output.replace('\n', '')
    file.close()
    return output
