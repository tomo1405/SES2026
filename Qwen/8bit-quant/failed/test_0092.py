import pytest
from src_0092 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mocking matplotlib to prevent actual plotting during tests
class MockAxes:
    def plot(self, *args, **kwargs):
        pass

    def legend(self):
        pass

@pytest.fixture
def mock_ax(mocker):
    mocker.patch('matplotlib.pyplot.subplots', return_value=(None, MockAxes()))
    return MockAxes()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]
    })

def test_task_func_with_valid_columns(sample_data, mock_ax):
    result, ax = task_func(sample_data, 'x', 'y')
    assert isinstance(result, tuple)
    assert len(result) == 5
    slope, intercept, r_value, p_value, std_err = result
    assert isinstance(slope, float)
    assert isinstance(intercept, float)
    assert isinstance(r_value, float)
    assert isinstance(p_value, float)
    assert isinstance(std_err, float)
    assert ax is not None

def test_task_func_with_invalid_column(sample_data, mock_ax):
    with pytest.raises(ValueError, match="Specified columns must exist in the DataFrame"):
        task_func(sample_data, 'x', 'z')

def test_task_func_with_empty_dataframe(mock_ax):
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError, match="Specified columns must exist in the DataFrame"):
        task_func(empty_df, 'x', 'y')