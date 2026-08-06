import pytest
from src_0157 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample DataFrame
    data = np.random.rand(10, 8)  # 10 samples, 8 features
    df, ax = task_func(data)
    
    # Check if the returned DataFrame has the correct shape
    assert df.shape == (10, 9), "DataFrame should have 10 rows and 9 columns"
    
    # Check if the returned DataFrame has the correct column names
    expected_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert list(df.columns) == expected_columns, "DataFrame columns do not match expected names"
    
    # Check if the 'Average' column is calculated correctly
    calculated_average = df.mean(axis=1)
    assert all(np.isclose(df['Average'], calculated_average)), "'Average' column calculation is incorrect"
    
    # Check if the returned Axes object is of the correct type
    assert isinstance(ax, plt.Axes), "Returned object is not a matplotlib Axes instance"
    
    # Check if the plot contains the 'Average' column data
    plotted_data = ax.get_lines()[0].get_ydata()
    assert all(np.isclose(plotted_data, df['Average'])), "Plot does not match 'Average' column data"

# Run the tests
if __name__ == "__main__":
    pytest.main()