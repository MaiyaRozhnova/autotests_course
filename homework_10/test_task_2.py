# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test1():
    assert all_division(100, 20) == 5


def test2():
    assert all_division(16, 2, 2, 2, 2) == 1.


@pytest.mark.smoke
def test3():
    with pytest.raises(ZeroDivisionError):
        all_division(5, 0, 1)


def test4():
    assert all_division(3, 1, 1) == 3


@pytest.mark.smoke
def test5():
    assert all_division(6542.542, 62.641, 2.368) == 44.10685978918048
