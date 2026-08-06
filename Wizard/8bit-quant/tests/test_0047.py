python
import pytest
from src_0047 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, 0.4472136, -1.3416407864998738],
                                'B': [-1.3416407864998738, 0.4472136, -1.3416407864998738],
                                'C': [-1.3416407864998738, 0.4472136, -1.3416407864998738]})
    expected_axes = [None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes
    
    # Test case 2: Test with missing values
    df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6], 'C': [7, 8, 9]})
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, 0.4472136, -1.3416407864998738],
                                'B': [-1.3416407864998738, 0.4472136, -1.3416407864998738],
                                'C': [-1.3416407864998738, 0.4472136, -1.3416407864998738]})
    expected_axes = [None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes
    
    # Test case 3: Test with all values missing
    df = pd.DataFrame({'A': [None, None, None], 'B': [None, None, None], 'C': [None, None, None]})
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, 0.4472136, -1.3416407864998738],
                                'B': [-1.3416407864998738, 0.4472136, -1.3416407864998738],
                                'C': [-1.3416407864998738, 0.4472136, -1.3416407864998738]})
    expected_axes = [None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes
    
    # Test case 4: Test with non-numeric columns
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f'], 'C': ['g', 'h', 'i']})
    expected_df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f'], 'C': ['g', 'h', 'i']})
    expected_axes = [None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes