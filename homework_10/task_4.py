# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import time
import pytest


@pytest.mark.usefixtures('print_class_time')
class TestClass:

    def test1(self):
        print('\nВыполняется тест1 ...')
        time.sleep(0.5)
        assert 2 == 2

    def test2(self, print_test_time):
        print('\nВыполняется тест2 ...')
        time.sleep(1.2)
        assert 0 == 0

    def test3(self):
        print('\nВыполняется тест3 ...')
        time.sleep(0.5)
        assert 1 == 1
