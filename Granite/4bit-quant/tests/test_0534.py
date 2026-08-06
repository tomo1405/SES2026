import pytest
from src_0534 import task_func

def test_task_func():
    num = '123'
    from_base = 10
    to_base = 2
    alphabet = '01'
    expected_output = ('b\'\\x96\\xa8\\x8c\\xf0\\x9e\\x98\\xb8\\x91\\xf0\\x9e\\x98\\xb8\\x91\\xf0\\x9e\\x98\\xb8\'', '96a88cf09e98b891f09e98b891f09e98b8')

    output = task_func(num, from_base, to_base, alphabet)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_invalid_to_base():
    num = '123'
    from_base = 10
    to_base = 1
    alphabet = '01'

    with pytest.raises(ValueError) as excinfo:
        task_func(num, from_base, to_base, alphabet)
    assert "to_base must be >= 2." in str(excinfo.value)