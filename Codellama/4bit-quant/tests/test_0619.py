import pandas as pd
from src_0619 import task_func


def test_task_func():
    # Test that the function returns a DataFrame and a list of two plots
    results, plots = task_func(10, 5)
    assert isinstance(results, pd.DataFrame)
    assert isinstance(plots, list)
    assert len(plots) == 2

    # Test that the DataFrame has the correct columns
    assert 'Team' in results.columns
    assert 'Goals' in results.columns
    assert 'Penalty Cost' in results.columns

    # Test that the plots have the correct x-axis labels
    assert plots[0].get_xlabel() == 'Team'
    assert plots[1].get_xlabel() == 'Team'

    # Test that the plots have the correct y-axis labels
    assert plots[0].get_ylabel() == 'Goals'
    assert plots[1].get_ylabel() == 'Penalty Cost'

    # Test that the plots have the correct colors
    assert plots[0].get_color() == 'viridis'
    assert plots[1].get_color() == 'viridis'

    # Test that the plots have the correct data
    assert plots[0].get_data() == results['Goals']
    assert plots[1].get_data() == results['Penalty Cost']