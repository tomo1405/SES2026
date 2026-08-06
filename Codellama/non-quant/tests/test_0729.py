import pytest
from src_0729 import task_func


def test_task_func():
    # Test with valid input
    data, converted_csv = task_func('test_data.csv', 'cp1251', 'utf8', ',')
    assert data == [{'Column': 'Value'}]
    assert converted_csv == 'Column,Value\n'

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func('test_data.csv', 'invalid_encoding', 'utf8', ',')

    with pytest.raises(ValueError):
        task_func('test_data.csv', 'cp1251', 'invalid_encoding', ',')

    with pytest.raises(ValueError):
        task_func('test_data.csv', 'cp1251', 'utf8', 'invalid_delimiter')