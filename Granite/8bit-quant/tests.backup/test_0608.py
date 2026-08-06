import pandas as pd
import matplotlib.pyplot as plt
from random import sample
from src_0608 import task_func
import pytest

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],
        'D': [10, 11, 12],
        'E': [13, 14, 15]
    })

    # Create a sample list of tuples
    tuples = [(1, 4), (2, 5)]

    # Call the function and store the returned values
    df_new, plots = task_func(df, tuples, 2)

    # Assert that the returned values are of the expected type
    assert isinstance(df_new, pd.DataFrame)
    assert isinstance(plots, list)

    # Assert that the DataFrame has the expected shape
    assert df_new.shape == (1, 5)

    # Assert that the list of plots has the expected length
    assert len(plots) == 2

    # Assert that the plots are of the expected type
    for plot in plots:
        assert isinstance(plot, plt.Axes)

if __name__ == "__main__":
    pytest.main()