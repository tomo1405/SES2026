import pandas as pd
from collections import Counter
from src_0903 import task_func
import pytest

def test_task_func():
    d = {'x': [1, 2, 3], 'y': [4, 5, 6], 'z': [7, 8, 9]}
    counts = task_func(d)
    assert isinstance(counts, dict)
    assert len(counts) == 3
    assert all(isinstance(c, Counter) for c in counts.values())
    d_empty = {'x': [], 'y': [], 'z': []}
    counts_empty = task_func(d_empty)
    assert all(len(c) == 0 for c in counts_empty.values())
    d_missing_key = {'x': [1, 2, 3]}
    counts_missing_key = task_func(d_missing_key)
    assert 'y' in counts_missing_key and 'z' in counts_missing_key
    assert len(counts_missing_key['y']) == 0 and len(counts_missing_key['z']) == 0