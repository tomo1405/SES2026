import numpy as np
import pandas as pd
from src_0690 import task_func


def test_task_func():
    # Create a sample DataFrame with numerical columns
    df = pd.DataFrame({
        'col1': np.random.normal(size=100),
        'col2': np.random.uniform(size=100),
        'col3': np.random.binomial(n=1, p=0.5, size=100)
    })

    # Call the function with the sample DataFrame
    p_values = task_func(df)

    # Assert that the returned dictionary contains the expected keys
    assert set(p_values.keys()) == set(df.columns)

    # Assert that the p-values are in the range [0, 1]
    for p_value in p_values.values():
        assert 0 <= p_value <= 1