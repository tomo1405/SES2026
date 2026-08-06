import pandas as pd
import pytest
import collections

def task_func(df):
    
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    df = df.drop_duplicates(subset='Customer')
    total_sales = df['Sales'].sum()
    popular_category = collections.Counter(df['Category']).most_common(1)[0][0]
    return {'Total Sales': total_sales, 'Most Popular Category': popular_category}

def test_task_func():
    # Test case 1: input is a DataFrame
    df = pd.DataFrame({'Customer': ['A', 'B', 'C'], 'Sales': [100, 200, 300], 'Category': ['X', 'Y', 'X']})
    expected_output = {'Total Sales': 600, 'Most Popular Category': 'X'}
    assert task_func(df) == expected_output

    # Test case 2: input is not a DataFrame
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

    # Test case 3: input DataFrame has no duplicates
    df = pd.DataFrame({'Customer': ['A', 'B', 'C'], 'Sales': [100, 200, 300], 'Category': ['X', 'X', 'Y']})
    expected_output = {'Total Sales': 600, 'Most Popular Category': 'X'}
    assert task_func(df) == expected_output