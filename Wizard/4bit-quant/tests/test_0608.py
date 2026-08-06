python
import pandas as pd
import matplotlib.pyplot as plt
from random import sample
from src_0608 import task_func

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})

    # Test removing tuples from DataFrame
    tuples = [('A', 'B'), ('C', 'D')]
    df_new, plots = task_func(df, tuples, 2)
    assert df_new.shape[0] == 3
    assert df_new.shape[1] == 4

    # Test generating plots
    assert len(plots) == 2
    for plot in plots:
        assert isinstance(plot, plt.Axes)