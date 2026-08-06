import pandas as pd
import pytest
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from src_0108 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'group': ['A', 'B', 'C', 'D', 'E'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'value': [10, 20, 30, 40, 50]
    })

def test_task_func_valid_input(sample_df):
    assert isinstance(task_func(sample_df), plt.Axes)

def test_task_func_empty_df(sample_df):
    sample_df = pd.DataFrame()
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_df)
    assert "DataFrame must be non-empty" in str(exc_info.value)

def test_task_func_missing_columns(sample_df):
    sample_df = sample_df.drop('group', axis=1)
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_df)
    assert "DataFrame must contain 'group', 'date', and 'value' columns" in str(exc_info.value)

def test_task_func_invalid_date_format(sample_df):
    sample_df['date'] = '2022-01-01'
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_df)
    assert "'date' column must be in datetime format" in str(exc_info.value)

def test_task_func_kmeans_params(sample_df):
    kmeans = KMeans(n_clusters=5, random_state=42)
    y_kmeans = kmeans.fit_predict(sample_df[['date', 'value']])
    assert task_func(sample_df, n_clusters=5, random_state=42).get_lines()[0].get_xdata().tolist() == sample_df['date'].apply(lambda x: x.toordinal()).tolist()
    assert task_func(sample_df, n_clusters=5, random_state=42).get_lines()[0].get_ydata().tolist() == sample_df['value'].tolist()