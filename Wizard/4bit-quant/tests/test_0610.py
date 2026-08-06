python
import pytest
from src_0610 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2
    
    expected_df = pd.DataFrame({'A': [1, 3], 'B': [4, 6], 'C': [7, 9], 'D': [10, 12], 'E': [13, 15]})
    expected_plots = [
        (('A', 'B'), ax),
        (('C', 'D'), ax)
    ]
    
    df, plots = task_func(df, tuples, n_plots)
    
    assert df.equals(expected_df)
    assert len(plots) == len(expected_plots)
    for plot, expected_plot in zip(plots, expected_plots):
        assert plot[0] == expected_plot[0]
        assert plot[1].get_xlabel() == expected_plot[1].get_xlabel()
        assert plot[1].get_ylabel() == expected_plot[1].get_ylabel()