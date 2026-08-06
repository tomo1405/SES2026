import os

from src_0675 import task_func


def test_task_func():
    # Test case 1: File does not exist
    filename = 'nonexistent_file.csv'
    expected_output = filename
    actual_output = task_func(filename)
    assert actual_output == expected_output

    # Test case 2: Empty file
    filename = 'empty_file.csv'
    with open(filename, 'w') as file:
        pass
    expected_output = filename
    actual_output = task_func(filename)
    assert actual_output == expected_output

    # Test case 3: Non-empty file
    filename = 'non_empty_file.csv'
    with open(filename, 'w') as file:
        file.write('column_1,column_2nvalue_1,value_2nvalue_3,value_4')
    expected_output = filename
    actual_output = task_func(filename)
    assert actual_output == expected_output

    # Clean up
    os.remove(filename)