# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('arg1, result', [pytest.param((100, 20), 5, marks=pytest.mark.smoke),
                                          ((16, 2, 2, 2, 2), 1),
                                          pytest.param((5, 0, 1), 0, marks=pytest.mark.skip('zero division')),
                                          ((3, 1, 1), 3),
                                          ((6542.542, 62.641, 2.368), 44.10685978918048)],
                         ids=['1', '2', '3', '4', '5'])
def test_all_division(arg1, result):
    assert all_division(*arg1) == result
