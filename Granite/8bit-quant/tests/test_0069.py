import pandas as pd
import seaborn as sns
import pytest

from src_0069 import task_func

def test_task_func():
    # Test case 1: Default arguments
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)

    # Test case 2: Custom arguments
    df, ax = task_func(data='/path/to/custom_data.csv', emp_prefix='CUSTOM')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)

    # Test case 3: Invalid data path
    with pytest.raises(FileNotFoundError):
        task_func(data='/path/to/invalid_data.csv')

    # Test case 4: Invalid employee prefix
    with pytest.raises(ValueError):
        task_func(emp_prefix='INVALID')