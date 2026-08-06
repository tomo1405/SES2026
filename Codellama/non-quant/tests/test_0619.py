import pandas as pd
import seaborn as sns
from src_0619 import task_func


def test_task_func():
    # Test that the function returns a DataFrame and a list of plots
    results, plots = task_func(5, 2)
    assert isinstance(results, pd.DataFrame)
    assert isinstance(plots, list)
    assert len(plots) == 2

    # Test that the DataFrame has the correct columns
    assert set(results.columns) == {'Team', 'Goals', 'Penalty Cost'}

    # Test that the plots are correct
    assert isinstance(plots[0], sns.barplot)
    assert isinstance(plots[1], sns.barplot)
    assert plots[0].x == 'Team'
    assert plots[0].y == 'Goals'
    assert plots[1].x == 'Team'
    assert plots[1].y == 'Penalty Cost'

    # Test that the plots have the correct data
    assert plots[0].data == results
    assert plots[1].data == results

    # Test that the plots have the correct palette
    assert plots[0].palette == 'viridis'
    assert plots[1].palette == 'viridis'