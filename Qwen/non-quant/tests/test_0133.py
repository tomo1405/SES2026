import binascii

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0133 import task_func


# Mocking plt.show to prevent actual plotting
class Mock:
    def __init__(self, *args, **kwargs):
        pass

    def savefig(self, *args, **kwargs):
        pass

plt.show = Mock

def test_task_func_valid_hex():
    hex_str = "48656c6c6f20576f726c64"
    df, ax = task_func(hex_str)
    
    expected_df = pd.DataFrame({
        'Byte Value': [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100],
        'Frequency': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    })
    
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_invalid_hex():
    hex_str = "Gibberish"
    with pytest.raises(ValueError, match="Invalid hex string"):
        task_func(hex_str)

def test_task_func_empty_hex():
    hex_str = ""
    with pytest.raises(binascii.Error):
        task_func(hex_str)

def test_task_func_single_byte():
    hex_str = "ff"
    df, ax = task_func(hex_str)
    
    expected_df = pd.DataFrame({
        'Byte Value': [255],
        'Frequency': [1]
    })
    
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_repeated_bytes():
    hex_str = "aabbccdd"
    df, ax = task_func(hex_str)
    
    expected_df = pd.DataFrame({
        'Byte Value': [169, 187, 204, 221],
        'Frequency': [2, 2, 2, 2]
    })
    
    pd.testing.assert_frame_equal(df, expected_df)