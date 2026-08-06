import matplotlib
import pandas as pd
from src_0610 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15], 'D': [4, 8, 12, 16, 20], 'E': [5, 10, 15, 20, 25]})
    tuples = [('A', 'B'), ('C', 'D'), ('E', 'A')]
    n_plots = 3

    df_out, plots = task_func(df, tuples, n_plots)

    assert len(plots) == n_plots
    for plot in plots:
        assert plot[0] in [('A', 'B'), ('C', 'D'), ('E', 'A')]
        assert isinstance(plot[1], matplotlib.axes.Axes)

    assert df_out.equals(df)