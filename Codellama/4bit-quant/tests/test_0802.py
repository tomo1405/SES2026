import pytest
from src_0802 import task_func

def test_task_func():
    # Test case 1: Empty file
    file_name = 'empty_file.csv'
    common_values = task_func(file_name)
    assert common_values == {}

    # Test case 2: Single row file
    file_name = 'single_row_file.csv'
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}

    # Test case 3: Multiple rows file
    file_name = 'multiple_rows_file.csv'
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}

    # Test case 4: File with missing values
    file_name = 'file_with_missing_values.csv'
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}

    # Test case 5: File with invalid values
    file_name = 'file_with_invalid_values.csv'
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}