import pandas as pd
import random
import pytest
from src_0882 import task_func

@pytest.fixture
def csv_file():
    return 'path/to/csv/file.csv'

def test_task_func_with_sample_size(csv_file):
    matches = task_func(csv_file, sample_size=10)
    assert len(matches) == 10

def test_task_func_with_pattern_and_sample_size(csv_file):
    matches = task_func(csv_file, pattern='[a-z]+', sample_size=5)
    assert len(matches) == 5
    assert all(matches['data'].str.contains('[a-z]+', na=False))

def test_task_func_with_invalid_pattern(csv_file):
    with pytest.raises(ValueError, match='Invalid pattern'):
        task_func(csv_file, pattern='[')

def test_task_func_with_negative_sample_size(csv_file):
    with pytest.raises(ValueError, match='Sample size must be a positive integer'):
        task_func(csv_file, sample_size=-10)