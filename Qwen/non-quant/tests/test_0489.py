import pytest
from src_0489 import task_func
import pandas as pd
import numpy as np

def test_task_func_invalid_period():
    with pytest.raises(ValueError):
        task_func(0, 1000, 1, 1, 0)

def test_task_func_invalid_step():
    with pytest.raises(ValueError):
        task_func(0, 1000, 0, 1, 1)

def test_task_func_zero_amplitude():
    ax = task_func(0, 1000, 1, 0, 1)
    df = pd.DataFrame(ax.get_lines()[0].get_xydata(), columns=["Timestamp", "Value"])
    assert (df["Value"] == 0).all()

def test_task_func_non_zero_amplitude():
    ax = task_func(0, 1000, 1, 1, 1)
    df = pd.DataFrame(ax.get_lines()[0].get_xydata(), columns=["Timestamp", "Value"])
    assert not (df["Value"] == 0).all()

def test_task_func_timestamp_format():
    ax = task_func(0, 1000, 1, 1, 1)
    df = pd.DataFrame(ax.get_lines()[0].get_xydata(), columns=["Timestamp", "Value"])
    assert all(isinstance(ts, str) and len(ts.split()) == 2 for ts in df["Timestamp"])

def test_task_func_length_of_data():
    ax = task_func(0, 1000, 1, 1, 1)
    df = pd.DataFrame(ax.get_lines()[0].get_xydata(), columns=["Timestamp", "Value"])
    assert len(df) == 1000