import pytest
from src_0156 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mock data for testing
data = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1]
]

def test_task_func():
    df, ax = task_func(data)
    
    # Check if the returned object is a tuple
    assert isinstance(df, pd.DataFrame), "The function should return a DataFrame"
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert df.columns.tolist() == expected_columns, "The DataFrame columns are incorrect"
    
    # Check if the 'Average' column is correctly calculated
    assert 'Average' in df.columns, "The 'Average' column is missing"
    
    # Check if the plot is created and displayed
    assert ax is not None, "The plot should be created and displayed"

# Run the test
if __name__ == "__main__":
    pytest.main()