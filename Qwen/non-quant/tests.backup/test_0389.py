import pytest
from src_0389 import task_func
import pandas as pd
import os

@pytest.fixture
def create_temp_csv_files(tmpdir):
    # Create temporary CSV files for testing
    file1 = tmpdir.join("file1.csv")
    file2 = tmpdir.join("file2.csv")
    
    data1 = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
    data2 = {'A': [4, 5, 6], 'B': ['d', 'e', 'f'], 'C': [7, 8, 9]}
    
    pd.DataFrame(data1).to_csv(file1, index=False)
    pd.DataFrame(data2).to_csv(file2, index=False)
    
    return [str(file1), str(file2)]

def test_task_func(create_temp_csv_files):
    my_tuple = ('A', 'B')
    path_csv_files = create_temp_csv_files
    
    result = task_func(my_tuple, path_csv_files)
    
    expected_counter_A = collections.Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
    expected_counter_B = collections.Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})
    
    assert result['A'] == expected_counter_A
    assert result['B'] == expected_counter_B
    assert 'C' not in result

def test_task_func_missing_column(create_temp_csv_files):
    my_tuple = ('A', 'D')
    path_csv_files = create_temp_csv_files
    
    result = task_func(my_tuple, path_csv_files)
    
    expected_counter_A = collections.Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
    expected_counter_D = collections.Counter()
    
    assert result['A'] == expected_counter_A
    assert result['D'] == expected_counter_D

def test_task_func_empty_files(tmpdir):
    my_tuple = ('A', 'B')
    path_csv_files = [str(tmpdir.join("empty1.csv")), str(tmpdir.join("empty2.csv"))]
    
    for file in path_csv_files:
        open(file, 'w').close()
    
    result = task_func(my_tuple, path_csv_files)
    
    expected_counter_A = collections.Counter()
    expected_counter_B = collections.Counter()
    
    assert result['A'] == expected_counter_A
    assert result['B'] == expected_counter_B