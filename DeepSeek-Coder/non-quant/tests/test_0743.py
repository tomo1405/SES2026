import pytest
from src_0743 import task_func

def test_empty_input():
    with pytest.raises(Exception) as e:
        task_func([])
    assert str(e.value) == 'The input array should not be empty.'

def test_non_numeric_values():
    with pytest.raises(ValueError) as e:
        task_func([('A', 'B'), ('C', 'D')])
    assert str(e.value) == 'The values have to be numeric.'

def test_valid_input():
    result = task_func([('A', 1), ('B', 2)])
    assert result['Value'].dtype == 'float64'