import pytest
from src_0804 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Input file has at least one numeric column
    file_name = "test_data.csv"
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_csv(file_name, index=False)
    result = task_func(file_name)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(df)

    # Test case 2: Input file has no numeric column
    file_name = "test_data_no_numeric.csv"
    df = pd.DataFrame({"A": ["a", "b", "c"], "B": ["d", "e", "f"]})
    df.to_csv(file_name, index=False)
    with pytest.raises(ValueError):
        task_func(file_name)

    # Test case 3: Input file has only one numeric column
    file_name = "test_data_one_numeric.csv"
    df = pd.DataFrame({"A": [1, 2, 3]})
    df.to_csv(file_name, index=False)
    result = task_func(file_name)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(df)

    # Test case 4: Input file has multiple numeric columns
    file_name = "test_data_multiple_numeric.csv"
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
    df.to_csv(file_name, index=False)
    result = task_func(file_name)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(df)