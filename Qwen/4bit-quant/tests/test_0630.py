import pytest
from src_0630 import task_func
import pandas as pd
import os
import shutil

@pytest.fixture(scope='module')
def setup_teardown():
    # Setup: Create a temporary directory for testing
    test_output_dir = './test_output'
    yield test_output_dir
    # Teardown: Remove the temporary directory after tests
    if os.path.exists(test_output_dir):
        shutil.rmtree(test_output_dir)

def test_task_func_with_single_dataframe(setup_teardown):
    dataset = [pd.DataFrame({'A': [1, 2], 'B': [3, 4]})]
    filename = 'test_file.csv'
    task_func(dataset, filename, output_dir=setup_teardown)
    assert os.path.exists(os.path.join(setup_teardown, filename))

def test_task_func_with_multiple_dataframes(setup_teardown):
    dataset = [
        pd.DataFrame({'A': [1, 2], 'B': [3, 4]}),
        pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
    ]
    filename = 'test_files.csv'
    task_func(dataset, filename, output_dir=setup_teardown)
    filepath = os.path.join(setup_teardown, filename)
    assert os.path.exists(filepath)
    with open(filepath, 'r') as f:
        content = f.read()
    expected_content = "A,B\n1,3\n2,4\n------\nC,D\n5,7\n6,8\n"
    assert content == expected_content

def test_task_func_nonexistent_output_dir(setup_teardown):
    non_existent_dir = './non_existent_dir'
    dataset = [pd.DataFrame({'A': [1, 2], 'B': [3, 4]})]
    filename = 'test_file.csv'
    task_func(dataset, filename, output_dir=non_existent_dir)
    assert os.path.exists(non_existent_dir)
    assert os.path.exists(os.path.join(non_existent_dir, filename))

def test_task_func_empty_dataset(setup_teardown):
    dataset = []
    filename = 'empty_file.csv'
    task_func(dataset, filename, output_dir=setup_teardown)
    assert not os.path.exists(os.path.join(setup_teardown, filename))