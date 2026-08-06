python
import pandas as pd
import pytest
from scipy.stats import chi2_contingency
from src_0885 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    p_value = task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900)
    assert p_value == 0.0
    
    # Test case 2: Invalid input - more than 3 columns specified
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'C', 'D'], larger=50, equal=900)
    
    # Test case 3: Invalid input - column not in DataFrame
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'D'], larger=50, equal=900)
    
    # Test case 4: Invalid input - no data meeting the conditions
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 901]})
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900)
    
    # Test case 5: Invalid input - contingency table is empty
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 901]})
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'C'], larger=100, equal=900)