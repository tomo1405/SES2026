import pytest
from src_0823 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(10, 2)
    assert len(result) == 10
    assert set(result) <= set(string.ascii_letters + string.digits)

    # Test case 2: Length is less than or equal to 0
    with pytest.raises(ValueError):
        task_func(-1, 2)

    # Test case 3: num_digits is greater than length
    with pytest.raises(ValueError):
        task_func(5, 6)

    # Test case 4: num_digits is 0
    result = task_func(5, 0)
    assert len(result) == 5
    assert all(char in string.ascii_letters for char in result)

    # Test case 5: num_digits is equal to length
    result = task_func(5, 5)
    assert len(result) == 5
    assert all(char in string.ascii_letters + string.digits for char in result)

    # Test case 6: Randomness test
    random.seed(42)
    result1 = task_func(10, 2)
    random.seed(42)
    result2 = task_func(10, 2)
    assert result1 == result2