import pytest
from src_0759 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func():
    # Test with default parameters
    result = task_func(num_samples=5)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 5, "The DataFrame should have 5 rows"
    assert set(result.columns) == {'Country', 'Age', 'Gender'}, "The DataFrame columns are incorrect"

    # Test with different parameters
    result = task_func(num_samples=10, countries=['USA', 'Canada'], ages=np.arange(25, 60, 5), genders=['Male', 'Female'], rng_seed=42)
    assert len(result) == 10, "The DataFrame should have 10 rows"
    assert set(result.columns) == {'Country', 'Age', 'Gender'}, "The DataFrame columns are incorrect"

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func('invalid_input')