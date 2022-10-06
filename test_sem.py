"""Тесты для анекдотов."""
from sem import cats_joke
from sem import corona_joke
from sem import military_joke
import pytest

tests1 = [(2, 'Озверин + Виагра. Месть кота Леопольда была ужасной.')]


@pytest.mark.parametrize('n_inp, resultat', tests1)
def testing_cats_joke(n_inp, resultat):
    """Тест анекдотов про кошек.

    Args:
        n_inp(int): номер анекдота
        resultat(string): анекдот
    """
    assert cats_joke(n_inp) == resultat


tests2 = [(2, 'Карантин — это военные сборы диванных войск.')]


@pytest.mark.parametrize('n_inp, resultat', tests2)
def testing_corona_joke(n_inp, resultat):
    """Тест анекдотов про ковид.

    Args:
        n_inp(int): номер анекдота
        resultat(string): анекдот
    """
    assert corona_joke(n_inp) == resultat


tests2 = [(2, 'Принять мужчину таким, какой он есть, может только военкомат.')]


@pytest.mark.parametrize('n_inp, resultat', tests2)
def testing_military_joke(n_inp, resultat):
    """Тест военных анекдотов.

    Args:
        n_inp(int): номер анекдота
        resultat(string): анекдот
    """
    assert military_joke(n_inp) == resultat
