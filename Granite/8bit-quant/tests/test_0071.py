import pandas as pd
import json
import numpy as np
from unittest.mock import patch, mock_open, MagicMock
from src_0071 import task_func

# Constants
COLUMNS = ['email', 'list']

def test_task_func():
    # Mock the open function to read a JSON file
    with patch('src_0071.open', mock_open(read_data='{"email": "example@example.com", "list": [1, 2, 3]}')):
        # Call the function and store the returned values
        df, ax = task_func('test.json')

        # Assert that the returned values are as expected
        assert isinstance(df, pd.DataFrame)
        assert df.columns.tolist() == COLUMNS + ["sum", "mean"]
        assert isinstance(ax, MagicMock)