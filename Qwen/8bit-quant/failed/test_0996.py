import pytest
from src_0996 import task_func
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# Mocking functions
def mock_read_csv_empty(*args, **kwargs):
    raise pd.errors.EmptyDataError("No data")

def mock_read_csv(*args, **kwargs):
    return pd.DataFrame([1, 2, 3, 4, 5])

def mock_isfile_true(*args, **kwargs):
    return True

def mock_isfile_false(*args, **kwargs):
    return False

def mock_savefig(*args, **kwargs):
    pass

def mock_close(*args, **kwargs):
    pass

@pytest.fixture(autouse=True)
def patch_os():
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(os.path, 'isfile', mock_isfile_true)
        yield

@pytest.fixture(autouse=True)
def patch_plt():
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(plt, 'savefig', mock_savefig)
        mp.setattr(plt, 'close', mock_close)
        yield

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv", "plot.png")

def test_task_func_empty_file():
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(pd, 'read_csv', mock_read_csv_empty)
        result = task_func("empty_file.csv", "plot.png")
        assert result == (np.nan, np.nan, "plot.png")

def test_task_func_valid_data():
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(pd, 'read_csv', mock_read_csv)
        result = task_func("valid_file.csv", "plot.png")
        assert result[0] == 3.0  # Mean of [1, 2, 3, 4, 5]
        assert result[1] == 3.0  # Median of [1, 2, 3, 4, 5]
        assert result[2] == "plot.png"

def test_task_func_non_numeric_data():
    data = StringIO("a\nb\nc")
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(pd, 'read_csv', lambda *args, **kwargs: pd.read_csv(data))
        result = task_func("non_numeric_file.csv", "plot.png")
        assert np.isnan(result[0])
        assert np.isnan(result[1])
        assert result[2] == "plot.png"