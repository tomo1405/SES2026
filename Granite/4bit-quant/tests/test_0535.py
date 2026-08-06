import pytest
from src_0535 import task_func

def test_task_func():
    num = '123'
    from_base = 10
    to_base = 2
    private_key = 'some_private_key'
    alphabet = '0123456789ABCDEF'

    expected_output = 'some_expected_output'

    actual_output = task_func(num, from_base, to_base, private_key, alphabet)

    assert actual_output == expected_output