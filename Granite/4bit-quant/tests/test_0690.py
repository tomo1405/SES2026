import numpy as np
import pandas as pd
import pytest
from scipy import stats


def task_func(df):

    p_values = {}

    for col in df.columns:
        column_data = np.array(df[col])
        
        test_stat, p_value = stats.shapiro(column_data)
        
        p_values[col] = p_value

    return p_values

def test_task_func():
    # Create a sample dataframe for testing
    df = pd.DataFrame({
        'col1': np.random.normal(size=100),
        'col2': np.random.uniform(size=100),
        'col3': np.random.randint(0, 10, size=100)
    })

    # Call the function with the sample dataframe
    p_values = task_func(df)

    # Assert that the returned p-values are between 0 and 1
    for p_value in p_values.values():
        assert 0 <= p_value <= 1

if __name__ == "__main__":
    pytest.main()