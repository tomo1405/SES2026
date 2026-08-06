import pandas as pd
from src_0387 import task_func


def test_task_func():
    # Test case 1: length = 10, min_value = 0, max_value = 100
    length = 10
    min_value = 0
    max_value = 100
    expected_output = pd.DataFrame({
        'Column1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column3': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column4': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column5': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    })
    output = task_func(length, min_value, max_value)
    pd.testing.assert_frame_equal(output, expected_output)

    # Test case 2: length = 10, min_value = 10, max_value = 90
    length = 10
    min_value = 10
    max_value = 90
    expected_output = pd.DataFrame({
        'Column1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column3': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column4': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column5': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    })
    output = task_func(length, min_value, max_value)
    pd.testing.assert_frame_equal(output, expected_output)

    # Test case 3: length = 10, min_value = 0, max_value = 100, with random seed
    length = 10
    min_value = 0
    max_value = 100
    expected_output = pd.DataFrame({
        'Column1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column3': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column4': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Column5': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    })
    output = task_func(length, min_value, max_value, random_state=42)
    pd.testing.assert_frame_equal(output, expected_output)