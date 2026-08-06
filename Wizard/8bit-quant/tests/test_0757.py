python
import shutil
from pathlib import Path
from typing import List
import pytest

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:

    if Path(source_dir).is_dir() == False:
        raise ValueError("source_dir does not exist.")

    if Path(target_dir).is_dir() == False:
        raise ValueError("target_dir does not exist.")

    count = 0

    for extension in extensions:
        for file_name in Path(source_dir).glob(f'*{extension}'):
            shutil.move(str(file_name), target_dir)
            count += 1

    return count

def test_task_func():
    # Test case 1: Valid input
    source_dir = 'tests/test_data/source_dir'
    target_dir = 'tests/test_data/target_dir'
    extensions = ['.txt', '.csv']
    expected_count = 2
    assert task_func(source_dir, target_dir, extensions) == expected_count

    # Test case 2: Invalid input - source_dir does not exist
    source_dir = 'tests/test_data/non_existent_dir'
    target_dir = 'tests/test_data/target_dir'
    extensions = ['.txt', '.csv']
    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, extensions)

    # Test case 3: Invalid input - target_dir does not exist
    source_dir = 'tests/test_data/source_dir'
    target_dir = 'tests/test_data/non_existent_dir'
    extensions = ['.txt', '.csv']
    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, extensions)

    # Test case 4: Invalid input - extensions is empty list
    source_dir = 'tests/test_data/source_dir'
    target_dir = 'tests/test_data/target_dir'
    extensions = []
    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, extensions)

    # Test case 5: Invalid input - extensions contains invalid extension
    source_dir = 'tests/test_data/source_dir'
    target_dir = 'tests/test_data/target_dir'
    extensions = ['.txt', '.csv', '.docx']
    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, extensions)