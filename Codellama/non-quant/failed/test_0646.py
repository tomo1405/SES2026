import pytest
from src_0646 import task_func

def test_task_func_with_valid_file():
    filename = "test_data.csv"
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    df.to_csv(filename, index=False)

    result = task_func(filename)

    assert result.equals(df)

def test_task_func_with_empty_file():
    filename = "test_data.csv"
    df = pd.DataFrame()
    df.to_csv(filename, index=False)

    result = task_func(filename)

    assert result.equals(df)

def test_task_func_with_invalid_file():
    filename = "invalid_file.csv"

    with pytest.raises(FileNotFoundError):
        task_func(filename)