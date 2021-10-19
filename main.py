"""Семинар 1 Функции. Семина2. Словари."""

from collections import Generator
from data_json import json


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


def example4(**param: str) -> None:
    """
    Семинар1, задание 4.

    :param param: Списко тегов.
    :return: Пустое значение.
    """
    if param.get('name') and param.get('city') and param.get('job'):
        print(f'''Имя={param.get('name')}''')
        print(f'''Город={param.get('city')}''')
        print(f'''Работа={param.get('job')}''')
    else:
        print('Ничего')


def waldo(js: dict) -> dict:
    """
    Семинар 2. Задание 3.

    :param js: Джейсончик
    :return: Значение Waldo
    """
    # Перебираем элементы словаря
    for el, val in js.items():
        type_val = str(type(val))
        # Если словарь, то нужно разложить на компоненты
        if type_val == '<class \'dict\'>':
            # Для раскладывания опять вызываем waldo
            result = waldo(val)
            if result:
                if result.get('Waldo'):
                    return result
        if type_val == '<class \'list\'>':
            result = waldo(dict(enumerate(val)))
            if result:
                if result.get('Waldo'):
                    return result
        if el == 'Waldo':
            return {el: val}
    return {'Ничего не найдено': '(((('}


print(waldo(json))
