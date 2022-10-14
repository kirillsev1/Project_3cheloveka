"""File with calling functions."""
from sem import military_joke, cats_joke, corona_joke


def main(number: int) -> str:
    """Function returns string from function.

    Args:
        number: int - number of choice function.

    Returns:
         str - answer.
    """
    try:
        files = ['military_joke', 'corona_joke', 'cats_joke']
        out = int(input('You have chosen a topic {0}. Choose a joke number from 1 to 3: \n'.format(files[number-1])))
    except ValueError:
        return 'ValueError'
    with open('military_joke.txt', 'r') as fir:
        if number == 1 and 1 <= out < len(fir.readlines()):
            return military_joke(out)
    with open('corona_joke.txt', 'r') as sec:
        if number == 2 and 1 <= out < len(sec.readlines()):
            return cats_joke(out)
    with open('cats.txt', 'r') as thi:
        if number == 3 and 1 <= out < len(thi.readlines()):
            return corona_joke(out)
    return 'Try again'


if __name__ == '__main__':
    while True:
        inp = input('1 - military jokes\n2 - corona jokes\n3 - cat jokes\nInput number from 1 to 3. To quit input q: \n')
        if inp == 'Q':
            break
        try:
            if 0 < int(inp) < 4:
                print(main(int(inp)))
            else:
                print('Try again')
        except ValueError:
            print('ValueError')
