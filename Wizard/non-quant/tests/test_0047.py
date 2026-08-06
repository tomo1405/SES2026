python
import pytest
from src_0047 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': ['a', 'b', 'c', 'd', 'e']})
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'B': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'C': ['a', 'b', 'c', 'd', 'e']})
    expected_axes = [None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes
    
    # Test case 2: Test with missing values
    df = pd.DataFrame({'A': [1, 2, 3, 4, None], 'B': [2, 4, 6, None, 10], 'C': ['a', 'b', 'c', None, 'e']})
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'B': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'C': ['a', 'b', 'c', None, 'e']})
    expected_axes = [None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes
    
    # Test case 3: Test with all values missing
    df = pd.DataFrame({'A': [None, None, None, None, None], 'B': [None, None, None, None, None], 'C': [None, None, None, None, None]})
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'B': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'C': ['a', 'b', 'c', None, 'e']})
    expected_axes = [None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes
    
    # Test case 4: Test with non-numeric columns
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': ['a', 'b', 'c', 'd', 'e'], 'D': ['f', 'g', 'h', 'i', 'j']})
    expected_df = pd.DataFrame({'A': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'B': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738],
                                'C': ['a', 'b', 'c', 'd', 'e'],
                                'D': ['f', 'g', 'h', 'i', 'j']})
    expected_axes = [None, None, None, None]
    result_df, result_axes = task_func(df)
    assert expected_df.equals(result_df)
    assert expected_axes == result_axes