import pytest
from src_0802 import task_func

def test_task_func_empty_file():
    file_name = 'empty_file.csv'
    with open(file_name, 'w') as f:
        f.write('')
    common_values = task_func(file_name)
    assert common_values == {}

def test_task_func_single_row():
    file_name = 'single_row.csv'
    with open(file_name, 'w') as f:
        f.write('1,2,3')
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}

def test_task_func_multiple_rows():
    file_name = 'multiple_rows.csv'
    with open(file_name, 'w') as f:
        f.write('1,2,3\n4,5,6')
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}

def test_task_func_multiple_rows_with_ties():
    file_name = 'multiple_rows_with_ties.csv'
    with open(file_name, 'w') as f:
        f.write('1,2,3\n4,5,6\n1,2,3')
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}

def test_task_func_multiple_rows_with_no_ties():
    file_name = 'multiple_rows_with_no_ties.csv'
    with open(file_name, 'w') as f:
        f.write('1,2,3\n4,5,6\n7,8,9')
    common_values = task_func(file_name)
    assert common_values == {'col1': 1, 'col2': 2, 'col3': 3}