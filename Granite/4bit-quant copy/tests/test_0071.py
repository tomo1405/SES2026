import pandas as pd
import json
import numpy as np
from unittest.mock import patch
from io import StringIO

# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    with open(json_file, 'r') as file:
        email_data = json.load(file)
    if not email_data:
        return pd.DataFrame([], columns=COLUMNS + ["sum", "mean"]), None

    df = pd.DataFrame(email_data, columns=COLUMNS)
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)

    ax = df[['sum', 'mean']].plot(kind='bar')

    return df, ax

def test_task_func():
    # Mock the json.load function to return a test data
    with patch('json.load', return_value=[{'email': 'test@example.com', 'list': [1, 2, 3]}]):
        # Mock the pd.DataFrame.plot function to return a dummy axis object
        with patch.object(pd.DataFrame, 'plot', return_value=None) as mock_plot:
            # Call the function with a test JSON file
            df, ax = task_func('test.json')
            # Assert that the returned DataFrame has the expected columns
            assert df.columns.tolist() == COLUMNS + ["sum", "mean"]
            # Assert that the returned axis object is not None
            assert ax is not None
            # Assert that the pd.DataFrame.plot function was called with the correct arguments
            mock_plot.assert_called_once_with(kind='bar')