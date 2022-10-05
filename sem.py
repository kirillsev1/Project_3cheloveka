def military_joke(n: int) -> str: 
    """This function return military joke
    n - joke number requested by the user
    """
    text = []
    file = open('military_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[n-1])
    if "\n" in output:
        output = output.replace('\n', '')
    return output

print(military_joke(3))

def corona_joke(n: int) -> str:
    """"This function return coronavirus joke
    n - joke number requested by the user
    """
    text = []
    file = open('corona_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[n-1])
    if "\n" in output:
        output = output.replace('\n', '')
    return output

def cats_joke(n: int) -> str:
    """"This function return cats joke
    n - joke number requested by the user
    """
    text = []
    file = open('cats_joke.txt', 'r')
    for line in file.readlines():
        text.append(line)
    output = ''.join(text[n-1])
    if "\n" in output:
        output = output.replace('\n', '')
    return output


