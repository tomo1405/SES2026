import pytest
from src_0126 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    result = task_func('abcdefghijklmnopqrstuvwxyz', 3)
    assert result.startswith('letter_combinations_') and result.endswith('.json')

    # Test case 2: Test with invalid input
    with pytest.raises(ValueError):
        task_func('abcd', 10)

    # Test case 3: Test with different input
    result = task_func('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)
    assert result.startswith('letter_combinations_') and result.endswith('.json')