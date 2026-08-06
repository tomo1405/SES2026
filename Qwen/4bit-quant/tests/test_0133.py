import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0133 import task_func


def test_task_func_valid_hex():
    hex_str = "48656c6c6f20576f726c64"
    df, ax = task_func(hex_str)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert 'Byte Value' in df.columns
    assert 'Frequency' in df.columns
    assert df['Byte Value'].equals(pd.Series([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100], dtype=np.uint8))
    assert df['Frequency'].equals(pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

def test_task_func_invalid_hex():
    hex_str = "48656c6l6f20576f726c64"
    with pytest.raises(ValueError, match="Invalid hex string"):
        task_func(hex_str)

def test_task_func_empty_hex():
    hex_str = ""
    df, ax = task_func(hex_str)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.empty
    assert ax.get_title() == 'Frequency of Bytes in Hex String'

def test_task_func_single_byte():
    hex_str = "ff"
    df, ax = task_func(hex_str)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert 'Byte Value' in df.columns
    assert 'Frequency' in df.columns
    assert df['Byte Value'].equals(pd.Series([255], dtype=np.uint8))
    assert df['Frequency'].equals(pd.Series([1]))