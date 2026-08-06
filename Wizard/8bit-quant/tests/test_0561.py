python
import pytest
from src_0561 import task_func

def test_task_func():
    # Test empty data
    with pytest.raises(ValueError):
        task_func('')

    # Test data with multiple years
    with pytest.raises(ValueError):
        task_func('2020-01-01,2021-01-01')

    # Test data with invalid format
    with pytest.raises(ValueError):
        task_func('2020-01-01,2021-01-01,2022-01-01')

    # Test data with valid format
    data = '2020-01-01,2020-02-01,2020-03-01,2020-04-01,2020-05-01,2020-06-01,2020-07-01,2020-08-01,2020-09-01,2020-10-01,2020-11-01,2020-12-01'
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)