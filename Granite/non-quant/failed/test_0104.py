import pytest
from src_0104 import task_func

def test_task_func():
    temperatures = pd.DataFrame({'temperature': [10, 20, 30, 40, 50]})
    ax = task_func(temperatures)
    assert ax is not None
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Temperature (°C)'
    assert ax.get_title() == 'Daily Temperatures in New York'

def test_task_func_with_empty_data():
    temperatures = pd.DataFrame()
    with pytest.raises(ValueError, match="Input temperatures must be a non-empty pandas DataFrame."):
        task_func(temperatures)

def test_task_func_with_invalid_data_type():
    temperatures = 'not a DataFrame'
    with pytest.raises(ValueError, match="Input temperatures must be a non-empty pandas DataFrame."):
        task_func(temperatures)