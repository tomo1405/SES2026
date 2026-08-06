python
import pandas as pd
import collections
import pytest

def task_func(df):
    
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    df = df.drop_duplicates(subset='Customer')
    total_sales = df['Sales'].sum()
    popular_category = collections.Counter(df['Category']).most_common(1)[0][0]
    return {'Total Sales': total_sales, 'Most Popular Category': popular_category}

def test_task_func():
    # Test case 1: Valid input DataFrame
    df = pd.DataFrame({'Customer': ['C1', 'C2', 'C3', 'C4'], 'Sales': [100, 200, 300, 400], 'Category': ['A', 'B', 'A', 'B']})
    expected_output = {'Total Sales': 1000, 'Most Popular Category': 'A'}
    assert task_func(df) == expected_output
    
    # Test case 2: Invalid input DataFrame
    df = 'Invalid input'
    with pytest.raises(ValueError):
        task_func(df)