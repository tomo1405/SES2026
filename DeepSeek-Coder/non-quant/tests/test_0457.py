import pytest
from src_0457 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Assuming the function is defined in src_0457 module

def test_task_func():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    })

    # Call the function
    normalized_data, ax = task_func(data)

    # Assertions to check the output
    assert isinstance(normalized_data, pd.DataFrame), "The output should be a DataFrame"
    assert isinstance(ax, plt.Axes), "The second output should be a matplotlib Axes object"
    assert len(normalized_data) == len(data), "The number of rows should remain the same"
    assert len(normalized_data.columns) == len(data.columns), "The number of columns should remain the same"

    # Additional assertions to check the heatmap
    assert ax is not None, "The heatmap should be plotted"

# Run the test
if __name__ == "__main__":
    pytest.main()