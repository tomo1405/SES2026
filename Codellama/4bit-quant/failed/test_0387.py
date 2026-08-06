import pytest
from src_0387 import task_func

def test_task_func():
    # Test case 1: length = 10, min_value = 0, max_value = 100
    length = 10
    min_value = 0
    max_value = 100
    expected_output = pd.DataFrame({
        'Column1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column2': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column3': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column4': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column5': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })
    output = task_func(length, min_value, max_value)
    assert output.equals(expected_output)

    # Test case 2: length = 10, min_value = 10, max_value = 100
    length = 10
    min_value = 10
    max_value = 100
    expected_output = pd.DataFrame({
        'Column1': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'Column2': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'Column3': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'Column4': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'Column5': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    })
    output = task_func(length, min_value, max_value)
    assert output.equals(expected_output)

    # Test case 3: length = 10, min_value = 0, max_value = 10
    length = 10
    min_value = 0
    max_value = 10
    expected_output = pd.DataFrame({
        'Column1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column2': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column3': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column4': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'Column5': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })
    output = task_func(length, min_value, max_value)
    assert output.equals(expected_output)