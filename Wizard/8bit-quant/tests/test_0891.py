python
import os
import random
import pandas as pd
import pytest

from src_0891 import task_func

@pytest.fixture
def data_dir():
    return 'data'

@pytest.fixture
def csv_files():
    return ['file1.csv', 'file2.csv', 'file3.csv']

@pytest.fixture
def seed():
    return 42

def test_task_func(data_dir, csv_files, seed):
    file, selected_rows = task_func(data_dir, csv_files, seed)
    assert isinstance(file, str)
    assert isinstance(selected_rows, pd.DataFrame)
    assert len(selected_rows) > 0
    assert len(selected_rows) <= len(pd.read_csv(os.path.join(data_dir, file)))