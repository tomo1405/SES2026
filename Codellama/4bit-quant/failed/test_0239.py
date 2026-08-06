import pytest
from src_0239 import task_func

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [20, 25, 30],
                   'Score': [80, 90, 70]})
    df, ax = task_func(df)
    assert df.equals(pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                                  'Age': [0, 1, 2],
                                  'Score': [0, 1, 0]})
    assert ax.get_xlabel() == 'Age (standardized)'
    assert ax.get_ylabel() == 'Score (standardized)'
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score'