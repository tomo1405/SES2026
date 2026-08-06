import pytest
from src_0176 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mocking the matplotlib functions to avoid actual plotting
class MockAx:
    def set_ylabel(self, label):
        pass

    def set_xticklabels(self, labels, rotation):
        pass

class MockFig:
    def subplots(self):
        return self, MockAx()

@pytest.fixture
def mock_plt(monkeypatch):
    mock_fig = MockFig()
    monkeypatch.setattr(plt, 'subplots', mock_fig.subplots)

def test_task_func_empty_df(mock_plt):
    df = pd.DataFrame()
    ax = task_func(df)
    assert isinstance(ax, MockAx)

def test_task_func_missing_columns(mock_plt):
    df = pd.DataFrame({'Likes': [100], 'Views': [200]})
    ax = task_func(df)
    assert isinstance(ax, MockAx)

def test_task_func_no_interesting_videos(mock_plt):
    df = pd.DataFrame({
        'Title': ['Uninteresting Video'],
        'Likes': [100],
        'Views': [200]
    })
    ax = task_func(df)
    assert isinstance(ax, MockAx)

def test_task_func_with_interesting_videos(mock_plt):
    df = pd.DataFrame({
        'Title': ['How to Code', 'What is Python'],
        'Likes': [150, 200],
        'Views': [300, 400]
    })
    ax = task_func(df)
    assert isinstance(ax, MockAx)
    assert 'Like Ratio' in df.columns
    assert df['Like Ratio'].tolist() == [0.5, 0.5]