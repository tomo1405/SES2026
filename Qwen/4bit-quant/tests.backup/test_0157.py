import pytest
from src_0157 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample DataFrame with random data
    data = np.random.rand(10, 8)  # 10 rows and 8 columns
    df, ax = task_func(data)
    
    # Check if the returned DataFrame has the correct shape
    assert df.shape == (10, 9), "The DataFrame should have 10 rows and 9 columns."
    
    # Check if the returned DataFrame has the correct column names
    expected_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert list(df.columns) == expected_columns, "The DataFrame should have the correct column names."
    
    # Check if the 'Average' column is calculated correctly
    df_copy = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    df_copy['Average'] = df_copy.mean(axis=1)
    assert df['Average'].equals(df_copy['Average']), "The 'Average' column should be calculated correctly."
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."
    
    # Check if the plot contains the correct data
    assert (ax.lines[0].get_xdata() == df.index).all(), "The x-axis of the plot should match the index of the DataFrame."
    assert (ax.lines[0].get_ydata() == df['Average']).all(), "The y-axis of the plot should match the 'Average' column of the DataFrame."

# Run the tests
if __name__ == "__main__":
    pytest.main()