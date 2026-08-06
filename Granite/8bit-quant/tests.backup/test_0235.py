import pandas as pd
import pytest
from scipy import stats
import matplotlib.pyplot as plt
from src_0235 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Name': ['John', 'Jane', 'John', 'Jane'],
        'Age': [25, 30, 25, 30],
        'Score': [80, 90, 85, 95]
    })

def test_input_type(sample_df):
    with pytest.raises(ValueError) as excinfo:
        task_func(sample_df.to_numpy())
    assert "The input df is not a DataFrame" in str(excinfo.value)

def test_drop_duplicates(sample_df):
    result_df = task_func(sample_df)
    assert len(result_df) == 2

def test_linear_regression(sample_df):
    result_df = task_func(sample_df)
    slope, intercept, r_value, _, _ = stats.linregress(result_df['Age'], result_df['Score'])
    assert slope != 0 and intercept != 0

def test_plot(sample_df):
    fig, ax = task_func(sample_df)
    assert isinstance(fig, plt.Figure) and isinstance(ax, plt.Axes)