"""File with calling functions."""
from sem import military_joke, cats_joke, corona_joke


def main(number: int) -> str:
    """Function returns string from function.

    Args:
        number: int - number of choice function.

    Returns:
         str - answer.
    """
    if number == 1:
        return military_joke(number)
    elif number == 2:
        return cats_joke(number)
    elif number == 3:
        return corona_joke(number)


if __name__ == '__main__':
    while True:
        inp = input('Input number from 1 to 3. To quit input Q: ')
        if inp == 'Q':
            break
        try:
            if 0 < int(inp) < 4:
                print(main(int(inp)))
        except ValueError:
            print('ValueError')
