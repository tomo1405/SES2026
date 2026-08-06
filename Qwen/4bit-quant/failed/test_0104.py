import pytest
from src_0104 import task_func
import pandas as pd

def test_task_func_with_empty_dataframe():
    temperatures = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(temperatures)
    assert str(excinfo.value) == "Input temperatures must be a non-empty pandas DataFrame."

def test_task_func_with_non_dataframe_input():
    temperatures = [1, 2, 3]
    with pytest.raises(ValueError) as excinfo:
        task_func(temperatures)
    assert str(excinfo.value) == "Input temperatures must be a non-empty pandas DataFrame."

def test_task_func_with_valid_dataframe():
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'temperature': [15, 18, 20]
    }
    temperatures = pd.DataFrame(data)
    temperatures['date'] = pd.to_datetime(temperatures['date'])
    temperatures.set_index('date', inplace=True)
    
    ax = task_func(temperatures)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Temperature (°C)'
    assert ax.get_title() == 'Daily Temperatures in New York'

def test_task_func_with_missing_temperature_column():
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03']
    }
    temperatures = pd.DataFrame(data)
    temperatures['date'] = pd.to_datetime(temperatures['date'])
    temperatures.set_index('date', inplace=True)
    
    with pytest.raises(KeyError) as excinfo:
        task_func(temperatures)
    assert str(excinfo.value) == "'temperature'"

def test_task_func_with_exception():
    data = {
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'temperature': [15, 18, 20]
    }
    temperatures = pd.DataFrame(data)
    temperatures['date'] = pd.to_datetime(temperatures['date'])
    temperatures.set_index('date', inplace=True)
    
    # Intentionally raise an exception in the plotting process
    def mock_plot(*args, **kwargs):
        raise Exception("Mocked exception")
    
    with pytest.raises(ValueError) as excinfo:
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(ax, 'plot', mock_plot)
            task_func(temperatures)
    assert str(excinfo.value) == "An error occurred: Mocked exception"