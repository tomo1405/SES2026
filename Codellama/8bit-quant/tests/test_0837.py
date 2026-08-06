import pytest
from src_0837 import task_func

def test_task_func():
    # Test case 1: target value found in first file
    target_value = '332'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    simulate = False
    result = task_func(target_value, csv_dir, processed_dir, simulate)
    assert result == {'file1.csv': 0}

    # Test case 2: target value found in second file
    target_value = '332'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    simulate = False
    result = task_func(target_value, csv_dir, processed_dir, simulate)
    assert result == {'file2.csv': 1}

    # Test case 3: target value not found
    target_value = '332'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    simulate = False
    result = task_func(target_value, csv_dir, processed_dir, simulate)
    assert result == {}

    # Test case 4: simulate=True
    target_value = '332'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    simulate = True
    result = task_func(target_value, csv_dir, processed_dir, simulate)
    assert result == {'file1.csv': 0, 'file2.csv': 1}