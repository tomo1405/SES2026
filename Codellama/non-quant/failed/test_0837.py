import pytest
from src_0837 import task_func

def test_task_func():
    # Test case 1: target value found in first file
    target_value = '332'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    result = task_func(target_value, csv_dir, processed_dir)
    assert result == {'file1.csv': 1}

    # Test case 2: target value found in second file
    target_value = '332'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    result = task_func(target_value, csv_dir, processed_dir)
    assert result == {'file2.csv': 2}

    # Test case 3: target value not found in any file
    target_value = '333'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    result = task_func(target_value, csv_dir, processed_dir)
    assert result == {}

    # Test case 4: simulate=True
    target_value = '332'
    csv_dir = './csv_files/'
    processed_dir = './processed_files/'
    result = task_func(target_value, csv_dir, processed_dir, simulate=True)
    assert result == {'file1.csv': 1, 'file2.csv': 2}