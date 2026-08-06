import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0141 import task_func
import pytest

def test_task_func():
    # Test case 1: df is not a DataFrame
    with pytest.raises(ValueError) as excinfo:
        task_func("not_a_df", ["col1", "col2"])
    assert "The input df must be a pandas DataFrame." in str(excinfo.value)

    # Test case 2: cols is not a list or contains non-string elements
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame(), ["col1", 2])
    assert "cols must be a list of column names." in str(excinfo.value)

    # Test case 3: cols contains non-existent columns
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame(), ["col1", "col2", "col3"])
    assert "All columns in cols must exist in the dataframe." in str(excinfo.value)

    # Test case 4: cols is an empty list
    df = pd.DataFrame()
    df["col1"] = [1, 2, 3]
    df["col2"] = [4, 5, 6]
    df_scaled = task_func(df, [])
    assert df_scaled.equals(df)

    # Test case 5: cols contains valid column names
    df = pd.DataFrame()
    df["col1"] = [1, 2, 3]
    df["col2"] = [4, 5, 6]
    df_scaled = task_func(df, ["col1", "col2"])
    scaler = StandardScaler()
    df_expected = df.copy()
    df_expected[["col1", "col2"]] = scaler.fit_transform(df[["col1", "col2"]])
    assert df_scaled.equals(df_expected)