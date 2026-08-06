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
    # Test case 1: source_dir does not exist
    with pytest.raises(ValueError):
        task_func('nonexistent_dir', 'target_dir', ['.txt'])

    # Test case 2: target_dir does not exist
    with pytest.raises(ValueError):
        task_func('source_dir', 'nonexistent_dir', ['.txt'])

    # Test case 3: source_dir and target_dir exist, but no files match the extensions
    assert task_func('source_dir', 'target_dir', ['.jpg']) == 0

    # Test case 4: source_dir and target_dir exist, and files match the extensions
    source_dir = 'tests/test_data/source_dir'
    target_dir = 'tests/test_data/target_dir'
    extensions = ['.txt', '.csv']
    expected_count = 2
    assert task_func(source_dir, target_dir, extensions) == expected_count

    # Test case 5: source_dir and target_dir exist, and files match the extensions, but target_dir is empty
    source_dir = 'tests/test_data/source_dir'
    target_dir = 'tests/test_data/empty_dir'
    extensions = ['.txt', '.csv']
    expected_count = 2
    assert task_func(source_dir, target_dir, extensions) == expected_count