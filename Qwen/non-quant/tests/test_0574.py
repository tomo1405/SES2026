import pytest
from src_0574 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    df, ax = task_func(array_length=10)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (3, 2), "DataFrame should have 3 rows and 2 columns"
    
    # Check if the DataFrame has the correct index
    expected_index = ['Mean', 'Median', 'Standard Deviation']
    assert all(df.index == expected_index), f"DataFrame index should be {expected_index}"
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Array1', 'Array2']
    assert all(df.columns == expected_columns), f"DataFrame columns should be {expected_columns}"
    
    # Check if the values in the DataFrame are numeric
    assert df.values.dtype == np.float64, "DataFrame values should be of type float64"
    
    # Check if the plot is a bar plot
    assert isinstance(ax, plt.Axes), "Return value should be a matplotlib Axes object"
    assert ax.get_kind() == 'bar', "Plot kind should be 'bar'"

# Run the tests
if __name__ == "__main__":
    pytest.main()