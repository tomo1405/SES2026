import pandas as pd
import seaborn as sns
import pytest

from src_0112 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Time': ['08:00', '12:00', '16:00'],
        'Temperature': [25, 28, 22]
    })

def test_invalid_df(sample_df):
    with pytest.raises(ValueError, match=r"Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns."):
        task_func(sample_df.drop(columns=['Date', 'Time']))

def test_valid_df(sample_df):
    ax = task_func(sample_df)
    assert ax.get_title() == 'Temperature Heatmap'