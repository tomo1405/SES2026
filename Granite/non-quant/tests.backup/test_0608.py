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
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [16, 17, 18, 19, 20],
        'E': [21, 22, 23, 24, 25]
    })

    # Create a sample list of tuples
    tuples = [(1, 6), (3, 8), (5, 10)]

    # Call the function and store the returned values
    df_result, plots_result = task_func(df, tuples, 3)

    # Assert that the returned DataFrame does not contain any of the tuples
    assert not df_result.apply(tuple, axis=1).isin(tuples).any()

    # Assert that the number of plots returned is equal to the specified number
    assert len(plots_result) == 3

    # Assert that the plots are of the correct type
    for plot in plots_result:
        assert isinstance(plot, plt.Axes)