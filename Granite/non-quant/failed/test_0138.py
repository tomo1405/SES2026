import pandas as pd
import pytest
from scipy.stats import skew
from src_0138 import task_func

def test_task_func():
    # Test case 1: Input is not a pandas DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func("not a DataFrame")
    assert "Input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 2: Input is an empty pandas DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        task_func(df)
    assert "Input must be a non-empty pandas DataFrame." in str(excinfo.value)

    # Test case 3: Input is a pandas DataFrame with valid data
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 4, 5, 6],
        'C': [3, 4, 5, 6, 7]
    })
    skewness = task_func(df)
    assert isinstance(skewness, float)

    # Test case 4: Input is a pandas DataFrame with NaN values
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 4, np.nan, 6],
        'C': [3, 4, 5, 6, 7]
    })
    skewness = task_func(df)
    assert isinstance(skewness, float)