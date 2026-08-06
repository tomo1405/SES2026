import pytest
from src_0269 import task_func

def test_task_func():
    n_keys = 5
    n_values = 10
    expected_output = {'e': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                       'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                       'f': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                       'b': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                       'c': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    actual_output = task_func(n_keys, n_values)
    assert actual_output == expected_output

if __name__ == "__main__":
    pytest.main()