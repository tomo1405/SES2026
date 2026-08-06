python
import pytest
from src_0612 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6], 'C': [3, 4, 5, 6, 7], 'D': [4, 5, 6, 7, 8], 'E': [5, 6, 7, 8, 9]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2
    
    expected_df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6], 'C': [3, 4, 5, 6, 7], 'D': [4, 5, 6, 7, 8], 'E': [5, 6, 7, 8, 9]})
    expected_plot_details = [('A', 'B'), ('C', 'D')]
    
    df, plot_details = task_func(df, tuples, n_plots)
    
    assert df.equals(expected_df)
    assert plot_details == expected_plot_details