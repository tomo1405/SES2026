import pandas as pd
import pytest
from src_0050 import task_func


def test_task_func_with_valid_timestamps():
    timestamps = [1633072800, 1633159200, 1633245600]  # Example timestamps
    df, ax = task_func(timestamps)
    
    assert isinstance(df, pd.DataFrame)
    assert "Timestamp" in df.columns
    assert "Datetime" in df.columns
    assert len(df) == len(timestamps)
    
    assert isinstance(ax, tuple)
    assert len(ax) == 2
    assert isinstance(ax[0], np.ndarray)  # Histogram counts
    assert isinstance(ax[1], np.ndarray)  # Bin edges

def test_task_func_with_empty_timestamps():
    with pytest.raises(ValueError) as exc_info:
        task_func([])
    
    assert str(exc_info.value) == "Input list of timestamps is empty."

def test_task_func_with_single_timestamp():
    timestamps = [1633072800]
    df, ax = task_func(timestamps)
    
    assert isinstance(df, pd.DataFrame)
    assert "Timestamp" in df.columns
    assert "Datetime" in df.columns
    assert len(df) == len(timestamps)
    
    assert isinstance(ax, tuple)
    assert len(ax) == 2
    assert isinstance(ax[0], np.ndarray)  # Histogram counts
    assert isinstance(ax[1], np.ndarray)  # Bin edges

def test_task_func_with_non_integer_timestamps():
    with pytest.raises(TypeError):
        task_func([1633072800.0, 'invalid', 1633245600])