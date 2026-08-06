import pytest
from src_0239 import task_func

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                      'Age': [25, 30, 35],
                      'Score': [90, 80, 70]})
    df, ax = task_func(df)
    assert df.equals(pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                                 'Age': [0.0, 0.5, 1.0],
                                 'Score': [0.9, 0.8, 0.7]}))
    assert ax.get_xlabel() == 'Age (standardized)'
    assert ax.get_ylabel() == 'Score (standardized)'
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score'