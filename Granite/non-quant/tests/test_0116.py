import numpy as np
import pytest
from src_0116 import task_func


def test_task_func():
    # Test case 1: Test with an empty list
    with pytest.raises(ValueError):
        task_func([])

    # Test case 2: Test with a list of numbers
    numbers = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 8, 9]
    expected_result = {'array': np.array([1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 8, 9]),
                       'mode': 5,
                       'entropy': 2.876116955209815}
    assert task_func(numbers) == expected_result

    # Test case 3: Test with a list of strings
    numbers = ['a', 'b', 'c', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'g', 'g', 'g']
    expected_result = {'array': np.array(['a', 'b', 'c', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'g', 'g', 'g']),
                       'mode': 'e',
                       'entropy': 2.876116955209815}
    assert task_func(numbers) == expected_result