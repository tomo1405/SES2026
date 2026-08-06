import re
import pandas as pd
from src_0484 import task_func

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'column_name': ['This is a test', 'Another test', 'Yet another test']
    })

    # Test case 1: pattern is not specified
    new_df = task_func(df, 'column_name', pattern=None)
    assert new_df.equals(df)

    # Test case 2: pattern is specified
    new_df = task_func(df, 'column_name', pattern='test')
    expected_df = pd.DataFrame({
        'column_name': ['sith si a tset', 'rehtona tset', 'etahY rehtona tset']
    })
    assert new_df.equals(expected_df)