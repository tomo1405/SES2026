import pytest
from src_0802 import task_func
import numpy as np
import os

# Helper function to create a temporary CSV file
def create_temp_csv(content, filename):
    with open(filename, 'w') as f:
        f.write(content)

@pytest.fixture
def temp_file(tmpdir):
    filename = tmpdir.join("temp.csv")
    yield str(filename)
    os.remove(str(filename))

def test_task_func_empty_file(temp_file):
    create_temp_csv("", temp_file)
    result = task_func(temp_file)
    assert result == {}

def test_task_func_single_row(temp_file):
    create_temp_csv("col1,col2\n1,2", temp_file)
    result = task_func(temp_file)
    assert result == {'col1': 1, 'col2': 2}

def test_task_func_multiple_rows_no_tie(temp_file):
    create_temp_csv("col1,col2\n1,2\n1,3\n1,4", temp_file)
    result = task_func(temp_file)
    assert result == {'col1': 1, 'col2': 2}

def test_task_func_multiple_rows_with_tie(temp_file):
    create_temp_csv("col1,col2\n1,2\n1,2\n2,3\n2,3", temp_file)
    result = task_func(temp_file)
    assert result == {'col1': 1, 'col2': 2}

def test_task_func_non_numeric_data(temp_file):
    create_temp_csv("col1,col2\na,b\na,c\nb,d", temp_file)
    result = task_func(temp_file)
    assert result == {'col1': 'a', 'col2': 'b'}

def test_task_func_mixed_data_types(temp_file):
    create_temp_csv("col1,col2\n1,a\n1,a\n2,b", temp_file)
    result = task_func(temp_file)
    assert result == {'col1': 1, 'col2': 'a'}