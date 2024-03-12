import pytest
from datetime import datetime


@pytest.fixture(scope='class')
def print_class_time():
    print('\nStart test class: ', datetime.now())
    yield
    print('\nEnd test class: ', datetime.now())


@pytest.fixture()
def print_test_time():
    start = datetime.now()
    yield
    print('\nTest time: ', datetime.now() - start)
