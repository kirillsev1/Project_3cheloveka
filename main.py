"""File with calling functions."""
from sem import military_joke, cats_joke, corona_joke


def output(num: int) -> int:
    """Function returns number of lines in file.

    Args:
        num: int - flag which makes choice from files.

    Returns:
        int: int - number of lines in chosen file.
    """
    if num == 1:
        with open('military_joke.txt', 'r') as fir:
            return len(fir.readlines())
    if num == 2:
        with open('corona_joke.txt', 'r') as sec:
            return len(sec.readlines())
    if num == 3:
        with open('cats.txt', 'r') as thi:
            return len(thi.readlines())


def main(number: int) -> str:
    """Function returns string from function.

    Args:
        number: int - number of choice function.

    Returns:
         str - answer.
    """
    length = output(number)
    text = 'You have chosen a topic {0}. Choose a joke number from 1 to {1}:\n'
    try:
        out = int(input(text.format(files[number - 1], length)))
    except ValueError:
        return 'ValueError'

    with open('military_joke.txt', 'r'):
        if number == 1 and 1 <= out <= length:
            return military_joke(out)
    with open('corona_joke.txt', 'r'):
        if number == 2 and 1 <= out <= length:
            return cats_joke(out)
    with open('cats.txt', 'r'):
        if number == 3 and 1 <= out < length:
            return corona_joke(out)
    return 'Try again'


if __name__ == '__main__':
    files = ['military_joke', 'corona_joke', 'cats_joke', 'Input number from 1 to 3. To quit input q:']
    while True:
        inp = input('1 - {0}\n2 - {1}\n3 - {2}\n{3} \n'.format(files[0], files[1], files[2], files[3]))
        if inp == 'Q':
            break
        try:
            if 0 < int(inp) < 4:
                print(main(int(inp)))
            else:
                print('Try again')
        except ValueError:
            print('ValueError')
