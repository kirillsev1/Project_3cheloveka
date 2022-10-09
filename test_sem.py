"""Тесты для анекдотов."""
from sem import cats_joke
from sem import corona_joke
from sem import military_joke
import pytest

with open ('cats.txt', 'r') as file:
    tests = []
    index = 0
    for line in file:
        index += 1
        tests.append((index, line[:-1:]))
    tests.pop()

    @pytest.mark.parametrize('n_inp, resultat', tests)
    def testing_cats_joke(n_inp, resultat):
        """Тест анекдотов про кошек.

        Args:
            n_inp(int): номер анекдота
            resultat(string): анекдот
        """
        assert cats_joke(n_inp) == resultat


with open ('corona_joke.txt', 'r') as file:
    tests = []
    index = 0
    for line in file:
        index += 1
        tests.append((index, line[:-1:]))
    tests.pop()


@pytest.mark.parametrize('n_inp, resultat', tests)
def testing_corona_joke(n_inp, resultat):
    """Тест анекдотов про ковид.

    Args:
        n_inp(int): номер анекдота
        resultat(string): анекдот
    """
    assert corona_joke(n_inp) == resultat


with open ('military_joke.txt', 'r') as file:
    tests = []
    index = 0
    for line in file:
        index += 1
        tests.append((index, line[:-1:]))
    tests.pop()


@pytest.mark.parametrize('n_inp, resultat', tests)
def testing_military_joke(n_inp, resultat):
    """Тест военных анекдотов.

    Args:
        n_inp(int): номер анекдота
        resultat(string): анекдот
    """
    assert military_joke(n_inp) == resultat
