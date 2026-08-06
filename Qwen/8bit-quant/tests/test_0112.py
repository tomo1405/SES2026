import pandas as pd
import pytest
import seaborn as sns
from src_0112 import task_func


@pytest.fixture
def sample_df():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'],
        'Time': ['12:00', '13:00', '14:00', '15:00'],
        'Temperature': [15, 16, 17, 18]
    }
    return pd.DataFrame(data)

def test_task_func_valid_input(sample_df):
    ax = task_func(sample_df)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert ax.get_title() == 'Temperature Heatmap'

def test_task_func_invalid_dataframe():
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns."):
        task_func(pd.DataFrame())

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'Date': ['2023-01-01'],
        'Time': ['12:00']
    })
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns."):
        task_func(df)

def test_task_func_non_dataframe():
    with pytest.raises(ValueError, match="Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns."):
        task_func([{'Date': '2023-01-01', 'Time': '12:00', 'Temperature': 15}])