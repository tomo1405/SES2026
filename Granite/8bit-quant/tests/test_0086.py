import pytest
from src_0086 import task_func

def test_task_func():
    # Test case 1: end_date is before start_date
    with pytest.raises(ValueError):
        task_func(start_date="2023-01-01", end_date="2022-12-31")

    # Test case 2: valid input
    df, ax = task_func(start_date="2022-01-01", end_date="2022-12-31")
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)