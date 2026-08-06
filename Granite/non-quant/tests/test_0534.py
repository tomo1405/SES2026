import pytest
from src_0534 import task_func

def test_task_func():
    num = '123'
    from_base = 10
    to_base = 2
    alphabet = '01'
    expected_output = ('Y6q1', '5e8b4d644f178362c80f')

    output = task_func(num, from_base, to_base, alphabet)
    assert output == expected_output, "Task function returned incorrect output"

def test_task_func_invalid_to_base():
    num = '123'
    from_base = 10
    to_base = 1
    alphabet = '01'

    with pytest.raises(ValueError) as excinfo:
        task_func(num, from_base, to_base, alphabet)
    assert "to_base must be >= 2." in str(excinfo.value), "Task function did not raise expected ValueError"