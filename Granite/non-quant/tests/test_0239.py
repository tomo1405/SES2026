import matplotlib
import pandas as pd
import pytest
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
    df_result, ax_result = task_func(df)
    assert isinstance(df_result, pd.DataFrame)
    assert isinstance(ax_result, matplotlib.axes.Axes)
    assert df_result.duplicated('Name').sum() == 0
    scaler = StandardScaler()
    df_standardized = df[['Age', 'Score']].copy()
    df_standardized[['Age', 'Score']] = scaler.fit_transform(df_standardized[['Age', 'Score']])
    assert df_result[['Age', 'Score']].equals(df_standardized)
    assert ax_result.get_xlabel() == 'Age (standardized)'
    assert ax_result.get_ylabel() == 'Score (standardized)'
    assert ax_result.get_title() == 'Scatter Plot of Standardized Age and Score'