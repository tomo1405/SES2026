python
import numpy as np
import scipy.stats as stats
import pytest

def task_func(df):

    p_values = {}

    for col in df.columns:
        column_data = np.array(df[col])
        
        test_stat, p_value = stats.shapiro(column_data)
        
        p_values[col] = p_value

    return p_values

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
    p_values = task_func(df)
    assert p_values['A'] > 0.05
    assert p_values['B'] > 0.05