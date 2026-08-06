import pytest
from src_0104 import task_func

def test_task_func():
    temperatures = pd.DataFrame({'temperature': [10, 20, 30, 40, 50]}, index=pd.date_range('2023-01-01', periods=5))
    ax = task_func(temperatures)
    assert ax is not None
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Temperature (°C)'
    assert ax.get_title() == 'Daily Temperatures in New York'

def test_task_func_with_empty_temperatures():
    temperatures = pd.DataFrame()
    with pytest.raises(ValueError, match="Input temperatures must be a non-empty pandas DataFrame."):
        task_func(temperatures)

def test_task_func_with_invalid_input():
    temperatures = 'invalid input'
    with pytest.raises(ValueError, match="Input temperatures must be a non-empty pandas DataFrame."):
        task_func(temperatures)