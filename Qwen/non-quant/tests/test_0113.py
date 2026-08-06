import pytest
from src_0113 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Status': ['Active', 'Inactive', 'Active', 'Pending', 'Inactive', 'Active']
    }
    return pd.DataFrame(data)

def test_task_func_input_validation(sample_df):
    # Test with correct input
    assert isinstance(task_func(sample_df), plt.Axes)

    # Test with non-DataFrame input
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    # Test with DataFrame missing 'Status' column
    df_missing_status = pd.DataFrame({'OtherColumn': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df_missing_status)

def test_task_func_plot(sample_df, monkeypatch):
    # Mock the plt.subplots and savefig methods to capture the plot
    class MockAxes:
        def pie(self, *args, **kwargs):
            pass

        def set_title(self, title):
            pass

    class MockFigure:
        def __init__(self):
            self.axes = MockAxes()

    class MockPyplot:
        def subplots(self):
            return MockFigure(), MockAxes()

        def savefig(self, fname, format=None):
            pass

    monkeypatch.setattr(plt, 'subplots', MockPyplot().subplots)
    monkeypatch.setattr(plt, 'savefig', MockPyplot().savefig)

    # Call the function and check if it returns an Axes object
    ax = task_func(sample_df)
    assert isinstance(ax, MockAxes)