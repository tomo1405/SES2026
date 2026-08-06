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
        'col1': [1, 2, 3, 4, 5],
        'col2': [6, 7, 8, 9, 10],
        'col3': [11, 12, 13, 14, 15]
    })
    skewness = task_func(df)
    assert isinstance(skewness, float)

    # Test case 4: Input is a pandas DataFrame with NaN values
    df = pd.DataFrame({
        'col1': [1, 2, 3, 4, 5],
        'col2': [6, 7, np.nan, 9, 10],
        'col3': [11, 12, 13, 14, 15]
    })
    skewness = task_func(df)
    assert isinstance(skewness, float)