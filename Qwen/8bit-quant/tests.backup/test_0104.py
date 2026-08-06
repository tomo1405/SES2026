import pytest
from src_0104 import task_func
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'temperature': [22, 23, 25, 21, 24]
    }
    index = pd.date_range(start='2023-01-01', periods=5)
    return pd.DataFrame(data, index=index)

def test_task_func_with_valid_data(sample_data):
    ax = task_func(sample_data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Daily Temperatures in New York'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Temperature (°C)'

def test_task_func_with_empty_dataframe():
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame())
    assert "Input temperatures must be a non-empty pandas DataFrame." in str(excinfo.value)

def test_task_func_with_non_dataframe_input():
    with pytest.raises(ValueError) as excinfo:
        task_func([1, 2, 3])
    assert "Input temperatures must be a non-empty pandas DataFrame." in str(excinfo.value)

def test_task_func_with_missing_column(sample_data):
    sample_data = sample_data.drop(columns=['temperature'])
    with pytest.raises(KeyError):
        task_func(sample_data)