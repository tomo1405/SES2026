import numpy as np
from scipy import stats
import pandas as pd

def task_func(df):

    p_values = {}

    for col in df.columns:
        column_data = np.array(df[col])
        
        test_stat, p_value = stats.shapiro(column_data)
        
        p_values[col] = p_value

    return p_values

def test_task_func():
    # Create a sample dataframe with numerical columns
    df = pd.DataFrame({
        'col1': np.random.normal(size=100),
        'col2': np.random.uniform(size=100),
        'col3': np.random.randint(0, 100, size=100)
    })

    # Call the function and store the returned p-values
    p_values = task_func(df)

    # Check if the returned p-values are valid
    assert isinstance(p_values, dict)
    assert len(p_values) == len(df.columns)
    for p_value in p_values.values():
        assert 0 <= p_value <= 1

def test_task_func_with_nan():
    # Create a sample dataframe with numerical columns and NaN values
    df = pd.DataFrame({
        'col1': np.random.normal(size=100),
        'col2': np.random.uniform(size=100),
        'col3': np.random.randint(0, 100, size=100)
    })
    df.iloc[0, 0] = np.nan

    # Call the function and store the returned p-values
    p_values = task_func(df)

    # Check if the returned p-values are valid
    assert isinstance(p_values, dict)
    assert len(p_values) == len(df.columns)
    for p_value in p_values.values():
        assert 0 <= p_value <= 1