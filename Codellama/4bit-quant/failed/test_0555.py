import pytest
from src_0555 import task_func

def test_task_func():
    # Test with valid inputs
    assert task_func(1, 5, ['apple', 'banana', 'cherry']) == 'apple banana cherry'
    assert task_func(2, 5, ['apple', 'banana', 'cherry']) == 'apple banana cherry'
    assert task_func(3, 5, ['apple', 'banana', 'cherry']) == 'apple banana cherry'
    assert task_func(4, 5, ['apple', 'banana', 'cherry']) == 'apple banana cherry'
    assert task_func(5, 5, ['apple', 'banana', 'cherry']) == 'apple banana cherry'

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(0, 5, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(6, 5, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(1, 0, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(1, 6, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(1, 5, [])

    # Test with valid inputs and invalid inputs
    assert task_func(1, 5, ['apple', 'banana', 'cherry']) == 'apple banana cherry'
    with pytest.raises(ValueError):
        task_func(0, 5, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(6, 5, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(1, 0, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(1, 6, ['apple', 'banana', 'cherry'])
    with pytest.raises(ValueError):
        task_func(1, 5, [])