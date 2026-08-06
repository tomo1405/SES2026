import json
from unittest.mock import mock_open, patch

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0071 import task_func

# Mocking the open and json.load functions to avoid reading files during testing

@patch('builtins.open', new_callable=mock_open, read_data='[{"email": "test@example.com", "list": [1, 2, 3]}]')
def test_task_func_with_data(mock_file):
    df, ax = task_func('dummy_file.json')
    
    # Check DataFrame structure
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['email', 'list', 'sum', 'mean']
    
    # Check DataFrame content
    assert df.loc[0, 'email'] == 'test@example.com'
    assert df.loc[0, 'list'] == [1, 2, 3]
    assert df.loc[0, 'sum'] == 6
    assert df.loc[0, 'mean'] == 2.0
    
    # Check plot
    assert isinstance(ax, plt.AxesSubplot)

@patch('builtins.open', new_callable=mock_open, read_data='[]')
def test_task_func_with_empty_data(mock_file):
    df, ax = task_func('dummy_file.json')
    
    # Check DataFrame structure
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['email', 'list', 'sum', 'mean']
    
    # Check DataFrame content
    assert df.empty
    
    # Check plot
    assert ax is None

@patch('builtins.open', new_callable=mock_open, side_effect=FileNotFoundError)
def test_task_func_with_nonexistent_file(mock_file):
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.json')

@patch('builtins.open', new_callable=mock_open, read_data='invalid_json')
def test_task_func_with_invalid_json(mock_file):
    with pytest.raises(json.JSONDecodeError):
        task_func('dummy_file.json')