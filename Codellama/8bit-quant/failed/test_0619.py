import pytest
from src_0619 import task_func

def test_task_func():
    # Test that the function returns a DataFrame and a list of plots
    results_df, plots = task_func(5, 2)
    assert isinstance(results_df, pd.DataFrame)
    assert isinstance(plots, list)
    assert len(plots) == 2

    # Test that the DataFrame has the correct columns
    assert 'Team' in results_df.columns
    assert 'Goals' in results_df.columns
    assert 'Penalty Cost' in results_df.columns

    # Test that the plots are correct
    assert isinstance(plots[0], sns.barplot)
    assert isinstance(plots[1], sns.barplot)
    assert plots[0].x == 'Team'
    assert plots[0].y == 'Goals'
    assert plots[1].x == 'Team'
    assert plots[1].y == 'Penalty Cost'

    # Test that the function raises an error if the number of goals or penalties is negative
    with pytest.raises(ValueError):
        task_func(-1, 2)
    with pytest.raises(ValueError):
        task_func(5, -2)