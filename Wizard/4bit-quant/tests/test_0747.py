python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pytest

def task_func(df, target_column, target_values=None):

    if not isinstance(df, pd.DataFrame):
        raise ValueError("df should be a DataFrame.")
    
    if df.empty:
        raise ValueError("df should contain at least one row")
    
    if target_column not in df.columns:
        raise ValueError("target_column should be in DataFrame")
    
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise ValueError("df values should be numeric only")

    if target_values != None:
        df = df.applymap(lambda x: x if x in target_values else 0)

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    model = LinearRegression().fit(X, y)

    return model

def test_task_func():
    # Test case 1: df is not a DataFrame
    with pytest.raises(ValueError):
        task_func("not a DataFrame", "target_column")

    # Test case 2: df is empty
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(), "target_column")

    # Test case 3: target_column is not in df
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]}), "target_column")

    # Test case 4: df values are not numeric
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]}), "col2")

    # Test case 5: target_values is not None
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    target_values = [1, 2]
    result = task_func(df, "col2", target_values)
    assert result.coef_[0] == 0

    # Test case 6: target_values is None
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    target_values = None
    result = task_func(df, "col2", target_values)
    assert result.coef_[0] == 1