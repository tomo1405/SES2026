import pytest
from src_0687 import task_func
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
    
    actual_output = task_func(list_of_lists)
    
    assert np.array_equal(actual_output, expected_output)

if __name__ == "__main__":
    pytest.main()