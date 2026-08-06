import pytest
from src_0108 import task_func
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Mocking the matplotlib.pyplot to capture plot creation
class MockPyplot:
    def __init__(self):
        self.title = None
        self.xlabel = None
        self.ylabel = None
        self.scatter_called_with = None

    def scatter(self, *args, **kwargs):
        self.scatter_called_with = args, kwargs

    def set_title(self, title):
        self.title = title

    def set_xlabel(self, xlabel):
        self.xlabel = xlabel

    def set_ylabel(self, ylabel):
        self.ylabel = ylabel

@pytest.fixture
def mock_pyplot(monkeypatch):
    mock_plt = MockPyplot()
    monkeypatch.setattr(plt, 'subplots', lambda: (mock_plt, mock_plt))
    return mock_plt

@pytest.fixture
def sample_df():
    data = {
        'group': ['A', 'A', 'B', 'B'],
        'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'value': [10, 20, 30, 40]
    }
    return pd.DataFrame(data)

def test_task_func_valid_input(sample_df, mock_pyplot):
    ax = task_func(sample_df)
    assert ax is not None
    assert mock_pyplot.title == 'KMeans Clustering of Value vs Date'
    assert mock_pyplot.xlabel == 'Date (ordinal)'
    assert mock_pyplot.ylabel == 'Value'
    assert mock_pyplot.scatter_called_with is not None

def test_task_func_empty_df(sample_df):
    with pytest.raises(ValueError, match="DataFrame must be non-empty"):
        task_func(sample_df.iloc[0:0])

def test_task_func_missing_column(sample_df):
    df_missing_group = sample_df.drop(columns=['group'])
    with pytest.raises(ValueError, match="DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."):
        task_func(df_missing_group)

def test_task_func_non_datetime_date(sample_df):
    df_invalid_date = sample_df.copy()
    df_invalid_date['date'] = df_invalid_date['date'].astype(str)
    with pytest.raises(ValueError, match="'date' column must be in datetime format."):
        task_func(df_invalid_date)