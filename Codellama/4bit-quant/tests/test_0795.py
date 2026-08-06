import pytest
from src_0795 import task_func

def test_task_func():
    # Test with valid inputs
    assert task_func(10) == 'abcdefghij'
    assert task_func(10, random_seed=1234) == 'abcdefghij'
    assert task_func(10, random_seed=5678) == 'abcdefghij'

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(0)
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func(10, random_seed=None)

def test_task_func_randomness():
    # Test that the function is random
    assert task_func(10, random_seed=1234) != task_func(10, random_seed=5678)
    assert task_func(10, random_seed=1234) != task_func(10, random_seed=1234)

if __name__ == '__main__':
    pytest.main()