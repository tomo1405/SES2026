from typing import Counter

import pytest
from src_0529 import task_func


def test_task_func():
    # Test with a valid CSV file
    file_path = "test_data.csv"
    duplicates, ax = task_func(file_path)
    assert duplicates == Counter({('a', 'b'): 2, ('c', 'd'): 3})
    assert ax.get_title() == "Duplicate Entries"
    assert ax.get_ylabel() == "Count"

    # Test with an invalid file format
    file_path = "test_data.txt"
    with pytest.raises(ValueError):
        task_func(file_path)

    # Test with an empty file
    file_path = "test_data_empty.csv"
    duplicates, ax = task_func(file_path)
    assert duplicates == Counter()
    assert ax is None