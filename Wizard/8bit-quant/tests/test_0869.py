python
import pytest
from src_0869 import task_func

def test_task_func():
    # Test case 1
    assert task_func(3) == ['Red', 'Green', 'Blue']

    # Test case 2
    assert task_func(5, rng_seed=42) == ['Green', 'Blue', 'Yellow', 'Purple', 'Red']

    # Test case 3
    assert task_func(10, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Black'], rng_seed=123) == ['Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Black', 'Red']

    # Test case 4
    with pytest.raises(ValueError):
        task_func(0)

    # Test case 5
    with pytest.raises(ValueError):
        task_func(-1)

    # Test case 6
    with pytest.raises(ValueError):
        task_func(11)

    # Test case 7
    with pytest.raises(ValueError):
        task_func(colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Black', 'White'])

    # Test case 8
    with pytest.raises(ValueError):
        task_func(colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Black', 'White', ''])

    # Test case 9
    with pytest.raises(ValueError):
        task_func(colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Black', 'White', ' '])

    # Test case 10
    with pytest.raises(ValueError):
        task_func(colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Gray', 'Black', 'White', ' ', ''])