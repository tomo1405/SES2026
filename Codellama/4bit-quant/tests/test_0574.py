import matplotlib
import numpy as np
import pandas as pd
from src_0574 import task_func


def test_task_func():
    # Test 1: Check if the function returns a tuple with two elements
    result = task_func()
    assert len(result) == 2

    # Test 2: Check if the first element of the tuple is a pandas DataFrame
    df, ax = result
    assert isinstance(df, pd.DataFrame)

    # Test 3: Check if the second element of the tuple is a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test 4: Check if the DataFrame has the correct index and columns
    expected_index = ['Mean', 'Median', 'Standard Deviation']
    expected_columns = ['Array1', 'Array2']
    assert df.index.equals(expected_index)
    assert df.columns.equals(expected_columns)

    # Test 5: Check if the DataFrame has the correct values
    expected_values = [[np.mean(array1), np.median(array1), np.std(array1)],
                       [np.mean(array2), np.median(array2), np.std(array2)]]
    assert np.allclose(df.values, expected_values)

    # Test 6: Check if the Axes object has the correct plot
    assert ax.get_title() == 'Statistics'
    assert ax.get_xlabel() == 'Array'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_xticks() == ['Array1', 'Array2']
    assert ax.get_yticks() == ['Mean', 'Median', 'Standard Deviation']