import pytest
from src_0104 import task_func
import pandas as pd

def test_task_func_valid_input():
    temperatures = pd.DataFrame({'temperature': [20, 22, 25, 20, 23, 19]}, index=pd.date_range('2022-01-01', '2022-01-06'))
    ax = task_func(temperatures)
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Temperature (°C)'
    assert ax.get_title() == 'Daily Temperatures in New York'
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_xdata() == temperatures.index
    assert ax.get_lines()[0].get_ydata() == temperatures['temperature']

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())
    with pytest.raises(ValueError):
        task_func(pd.Series())
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'temperature': [20, 22, 25, 20, 23, 19]}))
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'temperature': [20, 22, 25, 20, 23, 19]}, index=pd.date_range('2022-01-01', '2022-01-06'), columns=['temperature', 'humidity']))