import pytest
from src_0922 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Create a sample DataFrame
    data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]}
    df = pd.DataFrame(data)

    # Create a list of columns to normalize
    columns = ['col1', 'col2']

    # Call the task function
    df_copy = task_func(df, columns)

    # Check that the DataFrame has been normalized
    assert df_copy.equals(pd.DataFrame({'col1': [0.0, 0.5, 1.0, 1.5, 2.0], 'col2': [0.0, 0.5, 1.0, 1.5, 2.0]}))

    # Check that the original DataFrame has not been modified
    assert df.equals(pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]}))