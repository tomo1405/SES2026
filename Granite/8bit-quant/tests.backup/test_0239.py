import pytest
import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from src_0239 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'Name': ['John', 'Jane', 'John'],
        'Age': [25, 30, 25],
        'Score': [80, 90, 85]
    })

def test_task_func(df):
    result_df, ax = task_func(df)
    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_drop_duplicates(df):
    result_df, _ = task_func(df)
    assert len(result_df) == 2

def test_standard_scaler(df):
    result_df, _ = task_func(df)
    assert result_df['Age'].mean() == 0
    assert result_df['Age'].std() == 1
    assert result_df['Score'].mean() == 0
    assert result_df['Score'].std() == 1

def test_scatter_plot(df):
    _, ax = task_func(df)
    assert ax.get_xlabel() == 'Age (standardized)'
    assert ax.get_ylabel() == 'Score (standardized)'
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score'