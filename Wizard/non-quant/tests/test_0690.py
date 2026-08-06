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
    df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [5, 4, 3, 2, 1]})
    expected_p_values = {'col1': 0.9444444444444444, 'col2': 0.9444444444444444}
    p_values = task_func(df)
    assert p_values == expected_p_values