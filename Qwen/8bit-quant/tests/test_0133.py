import pytest
from src_0133 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_valid_hex():
    hex_str = "48656c6c6f20576f726c64"
    df, ax = task_func(hex_str)
    
    # Check DataFrame
    expected_df = pd.DataFrame({
        'Byte Value': [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100],
        'Frequency': [1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1]
    })
    pd.testing.assert_frame_equal(df.sort_values(by='Byte Value').reset_index(drop=True), expected_df.sort_values(by='Byte Value').reset_index(drop=True))
    
    # Check plot
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_hex():
    hex_str = "GHIJKL"
    with pytest.raises(ValueError, match="Invalid hex string"):
        task_func(hex_str)

def test_task_func_empty_hex():
    hex_str = ""
    df, ax = task_func(hex_str)
    
    # Check DataFrame
    expected_df = pd.DataFrame(columns=['Byte Value', 'Frequency'])
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check plot
    assert isinstance(ax, plt.Axes)

def test_task_func_single_byte():
    hex_str = "FF"
    df, ax = task_func(hex_str)
    
    # Check DataFrame
    expected_df = pd.DataFrame({
        'Byte Value': [255],
        'Frequency': [1]
    })
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check plot
    assert isinstance(ax, plt.Axes)