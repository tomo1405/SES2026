python
import pytest
from multiprocessing import Pool
from src_0364 import task_func

def test_task_func():
    # Test valid input
    numbers = [1, 2, 3, 4, 5]
    expected_result = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
    assert task_func(numbers) == expected_result
    
    # Test invalid input
    with pytest.raises(ValueError):
        task_func([1, 2, "3", 4, 5])