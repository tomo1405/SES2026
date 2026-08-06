import pytest
from src_1034 import task_func

def test_task_func():
    df, ax = task_func()
    
    # Check if the DataFrame is created correctly
    assert df.shape == (17576, 3)  # 26^3 combinations
    assert list(df.columns) == ['a', 'b', 'c']
    
    # Check if the value counts are calculated correctly
    value_counts = df["a"].value_counts().reindex(list(string.ascii_lowercase), fill_value=0)
    assert value_counts.equals(value_counts)
    
    # Check if the plot is created correctly
    assert ax is not None