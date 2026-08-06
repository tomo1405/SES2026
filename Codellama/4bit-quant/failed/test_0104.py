import pytest
from src_0104 import task_func
import matplotlib.pyplot as plt
import pandas as pd

def test_task_func():
    temperatures = pd.DataFrame({'temperature': [23, 24, 25, 26, 27]}, index=pd.date_range('2022-01-01', '2022-01-05'))
    ax = task_func(temperatures)
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Temperature (°C)'
    assert ax.get_title() == 'Daily Temperatures in New York'
    assert ax.get_lines()[0].get_data() == (temperatures.index, temperatures['temperature'])

def test_task_func_empty_input():
    temperatures = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(temperatures)

def test_task_func_invalid_input():
    temperatures = 'invalid input'
    with pytest.raises(ValueError):
        task_func(temperatures)