import pytest
from src_0996 import task_func
import os
import pandas as pd
import numpy as np

# Mocking the required modules for testing
@pytest.fixture
def mock_file_path(tmpdir):
    file_path = tmpdir.join("test_data.csv")
    return str(file_path)

@pytest.fixture
def mock_plot_path(tmpdir):
    plot_path = tmpdir.join("test_plot.png")
    return str(plot_path)

def test_task_func_file_not_found(mock_file_path, mock_plot_path, monkeypatch):
    def mock_isfile(path):
        return False
    monkeypatch.setattr(os.path, "isfile", mock_isfile)
    
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(mock_file_path, mock_plot_path)
    assert str(excinfo.value) == f"File {mock_file_path} does not exist."

def test_task_func_empty_file(mock_file_path, mock_plot_path, monkeypatch):
    def mock_read_csv(path):
        raise pd.errors.EmptyDataError()
    monkeypatch.setattr(pd, "read_csv", mock_read_csv)
    
    mean, median, plot_path = task_func(mock_file_path, mock_plot_path)
    assert np.isnan(mean)
    assert np.isnan(median)
    assert plot_path == mock_plot_path

def test_task_func_valid_data(mock_file_path, mock_plot_path, monkeypatch):
    def mock_read_csv(path):
        return pd.DataFrame([1, 2, 3, 4, 5])
    monkeypatch.setattr(pd, "read_csv", mock_read_csv)
    
    mean, median, plot_path = task_func(mock_file_path, mock_plot_path)
    assert mean == 3.0
    assert median == 3.0
    assert plot_path == mock_plot_path
    assert os.path.exists(plot_path)

def test_task_func_non_numeric_data(mock_file_path, mock_plot_path, monkeypatch):
    def mock_read_csv(path):
        return pd.DataFrame(["a", "b", "c"])
    monkeypatch.setattr(pd, "read_csv", mock_read_csv)
    
    mean, median, plot_path = task_func(mock_file_path, mock_plot_path)
    assert np.isnan(mean)
    assert np.isnan(median)
    assert plot_path == mock_plot_path

def test_task_func_all_nan_data(mock_file_path, mock_plot_path, monkeypatch):
    def mock_read_csv(path):
        return pd.DataFrame([np.nan, np.nan, np.nan])
    monkeypatch.setattr(pd, "read_csv", mock_read_csv)
    
    mean, median, plot_path = task_func(mock_file_path, mock_plot_path)
    assert np.isnan(mean)
    assert np.isnan(median)
    assert plot_path == mock_plot_path