import pytest
from src_0967 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)

    # Call the function
    result, fig = task_func(df)

    # Assert the result
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert isinstance(fig, plt.Figure), "The figure should be a matplotlib figure"

    # Additional assertions can be added to check the content of the DataFrame and the plot