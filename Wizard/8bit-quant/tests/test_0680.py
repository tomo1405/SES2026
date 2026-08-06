python
import pandas as pd
from collections import Counter
import pytest

def task_func(df):
    df['combination'] = pd.Series(df.apply(lambda row: tuple(sorted(row)), axis=1))
    
    # Using Counter from collections to calculate the frequency of each combination
    combination_freq = Counter(df['combination'])
    
    return dict(combination_freq)

def test_task_func():
    # Test case 1
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_result = {((1, 4),): 1, ((1, 5),): 1, ((1, 6),): 1, ((2, 4),): 1, ((2, 5),): 1, ((2, 6),): 1, ((3, 4),): 1, ((3, 5),): 1, ((3, 6),): 1}
    assert task_func(df) == expected_result
    
    # Test case 2
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [3, 4, 5]})
    expected_result = {((1, 3),): 1, ((1, 4),): 1, ((1, 5),): 1, ((2, 3),): 1, ((2, 4),): 1, ((2, 5),): 1, ((3, 3),): 1, ((3, 4),): 1, ((3, 5),): 1}
    assert task_func(df) == expected_result
    
    # Test case 3
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 3]})
    expected_result = {((1, 1),): 1, ((1, 2),): 1, ((1, 3),): 1, ((2, 1),): 1, ((2, 2),): 1, ((2, 3),): 1, ((3, 1),): 1, ((3, 2),): 1, ((3, 3),): 1}
    assert task_func(df) == expected_result