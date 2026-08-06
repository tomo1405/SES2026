import pandas as pd
import matplotlib.pyplot as plt
from random import sample
from src_0608 import task_func

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 20, 30, 40, 50],
        'D': [50, 40, 30, 20, 10],
        'E': [100, 200, 300, 400, 500]
    })

    # Create a sample list of tuples
    tuples = [(1, 5), (3, 2), (5, 1)]

    # Call the function with the sample inputs
    df_output, plots_output = task_func(df, tuples, 3)

    # Assert the output types
    assert isinstance(df_output, pd.DataFrame)
    assert isinstance(plots_output, list)

    # Assert the output values
    assert df_output.shape == (2, 5)
    assert len(plots_output) == 3
    for ax in plots_output:
        assert isinstance(ax, plt.Axes)