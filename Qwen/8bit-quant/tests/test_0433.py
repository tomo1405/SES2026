import pandas as pd
import pytest
from src_0433 import task_func

# Mock data for testing
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature1': ['A', 'B', 'A', 'B']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'feature2': ['X', 'Y', 'X', 'Y']
})

def test_task_func():
    p_value, heatmap = task_func(df1, df2)
    assert isinstance(p_value, float)
    assert isinstance(heatmap, sns.axisgrid.FacetGrid)

def test_task_func_with_different_columns():
    p_value, heatmap = task_func(df1, df2, column1='feature1', column2='feature2')
    assert isinstance(p_value, float)
    assert isinstance(heatmap, sns.axisgrid.FacetGrid)

def test_task_func_with_missing_id():
    df1_missing = pd.DataFrame({
        'id': [1, 2, 5],
        'feature1': ['A', 'B', 'A']
    })
    with pytest.raises(KeyError):
        task_func(df1_missing, df2)

def test_task_func_with_empty_dataframes():
    empty_df1 = pd.DataFrame(columns=['id', 'feature1'])
    empty_df2 = pd.DataFrame(columns=['id', 'feature2'])
    with pytest.raises(ValueError):
        task_func(empty_df1, empty_df2)