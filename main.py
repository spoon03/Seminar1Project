"""Семинар 1."""

from collections import Generator


def my_gen_1(a: int, b: int) -> Generator:
    """
    Семинар1.Задание 1.

    :param a: Начало интервала. 1 в задании
    :param b: Конец интервала. 20 в задании
    :return: Возвращает квадрат либо куб числа.
    """
    r = range(a, b + 1)
    for i in r:
        n = list(str(i))
        sum_dig = sum([int(dig) for dig in n])
        if i % 2 == 0 or sum_dig % 2 == 0:
            y = i ** 2
        else:
            y = i ** 3
        yield y


def my_gen_fib_2(n: int) -> Generator:
    """
    Семинар 1.Задание 2.

    :param n: Кол-во элементов последовательности.
    :return: Возвращает фибоначи.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def validation(text: str, *suffix: str) -> bool:
    """
    Семинар 1.Задание 2.

    :param text: Строка для проверки.
    :param suffix: Набор фуффиксов для поиска в строке.
    :return: Если найден хоть один то true.
    """
    result = {}
    separate = text.split('_')
    for sf in suffix:
        for pos in separate:
            if pos == sf:
                result[sf] = True
                break
            else:
                result[sf] = False
    for v in result.values():
        if not v:
            return False
            break
    return True


print(validation('qwe_rty_ttt1_yyy', 'qwe', 'rty', 'ttt'))
