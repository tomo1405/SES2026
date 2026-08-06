python
import pytest
from src_0561 import task_func

def test_task_func_valid_data():
    data = '2021-01-01,2021-02-02,2021-03-03'
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func('')

def test_task_func_multiple_years():
    data = '2021-01-01,2022-02-02,2023-03-03'
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_invalid_date_format():
    data = '2021-01-01,2021-02-02,2021-03-03,2021-04-04-04'
    with pytest.raises(ValueError):
        task_func(data)