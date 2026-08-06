import pytest
from src_0111 import task_func
import pandas as pd
import io
import sys

# Mocking plt.show to prevent actual plotting during tests
class MockPlot:
    def show(self):
        pass

@pytest.fixture(autouse=True)
def mock_plot(monkeypatch):
    monkeypatch.setattr(plt, 'show', MockPlot().show)

def test_task_func_valid_data():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-02'],
        'Sales': [100, 200, 150]
    }
    df = pd.DataFrame(data)
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Daily Turnover'
    assert ax.get_ylabel() == 'Sales'

def test_task_func_invalid_dataframe():
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns."):
        task_func([])

def test_task_func_missing_columns():
    data = {
        'Date': ['2023-01-01', '2023-01-02']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns."):
        task_func(df)

def test_task_func_empty_resampled_data():
    data = {
        'Date': ['2023-01-01'],
        'Sales': [0]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError, match="No data available to plot after resampling."):
        task_func(df)