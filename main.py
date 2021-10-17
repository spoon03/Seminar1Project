"""Семинар 1.Задания 1 и 2."""

from collections import Generator


def my_gen_1(a: int, b: int) -> Generator:
    """
    Семинар1.Задание 1.

    :param a: Начало интервала. 1 в задании
    :param b: Конец интервала. 2 в задании
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


for k in my_gen_fib_2(10):
    print(k)
