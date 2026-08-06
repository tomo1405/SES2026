import pytest
from src_0812 import task_func

def test_task_func_no_sample():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    item = 2
    expected_positions = [(1, 'A')]
    expected_dataframe = pd.DataFrame(data)
    
    positions, dataframe = task_func(data, item)
    
    assert positions == expected_positions
    assert dataframe.equals(expected_dataframe)

def test_task_func_with_sample():
    data = {'A': [1, 2, 3, 2], 'B': [4, 5, 6, 2]}
    item = 2
    sample_size = 2
    random_seed = 42
    expected_positions = [(1, 'A'), (3, 'A'), (1, 'B'), (3, 'B')]
    
    positions, dataframe = task_func(data, item, sample_size, random_seed)
    
    assert len(positions) == sample_size
    assert all(pos in expected_positions for pos in positions)
    assert dataframe.equals(pd.DataFrame(data))

def test_task_func_no_matches():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    item = 7
    expected_positions = []
    expected_dataframe = pd.DataFrame(data)
    
    positions, dataframe = task_func(data, item)
    
    assert positions == expected_positions
    assert dataframe.equals(expected_dataframe)

def test_task_func_empty_data():
    data = {}
    item = 1
    expected_positions = []
    expected_dataframe = pd.DataFrame(data)
    
    positions, dataframe = task_func(data, item)
    
    assert positions == expected_positions
    assert dataframe.equals(expected_dataframe)

def test_task_func_large_sample_size():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    item = 2
    sample_size = 10
    expected_positions = [(1, 'A')]
    expected_dataframe = pd.DataFrame(data)
    
    positions, dataframe = task_func(data, item, sample_size)
    
    assert len(positions) == len(expected_positions)
    assert all(pos in expected_positions for pos in positions)
    assert dataframe.equals(expected_dataframe)