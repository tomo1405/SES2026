import pandas as pd
from src_0617 import task_func


def test_task_func():
    # Test with default parameters
    results_df, ax = task_func(10, 5)
    assert results_df.equals(pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                                          'Goals': [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)],
                                          'Penalty Cost': [randint(0, 10) * 1000, randint(0, 10) * 1000, randint(0, 10) * 1000, randint(0, 10) * 1000, randint(0, 10) * 1000]},
                                         index=['Team A', 'Team B', 'Team C', 'Team D', 'Team E']))
    assert ax.get_ylabel() == 'Results'

    # Test with custom parameters
    results_df, ax = task_func(10, 5, ['Team A', 'Team B', 'Team C'], 500, 1234)
    assert results_df.equals(pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C'],
                                          'Goals': [randint(0, 10), randint(0, 10), randint(0, 10)],
                                          'Penalty Cost': [randint(0, 10) * 500, randint(0, 10) * 500, randint(0, 10) * 500]},
                                         index=['Team A', 'Team B', 'Team C']))
    assert ax.get_ylabel() == 'Results'

    # Test with negative goals and penalties
    results_df, ax = task_func(-10, -5)
    assert results_df.equals(pd.DataFrame({'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
                                          'Goals': [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)],
                                          'Penalty Cost': [randint(0, 10) * 1000, randint(0, 10) * 1000, randint(0, 10) * 1000, randint(0, 10) * 1000, randint(0, 10) * 1000]},
                                         index=['Team A', 'Team B', 'Team C', 'Team D', 'Team E']))
    assert ax.get_ylabel() == 'Results'