import pytest
from src_0791 import task_func

def test_task_func():
    # Test case 1: Ensure provided columns exist in the dataframe
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df, "col3", "col4")

    # Test case 2: Ensure the output is a list of indices
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    output = task_func(df, "col1", "col2")
    assert isinstance(output, list)
    assert all(isinstance(i, int) for i in output)

    # Test case 3: Ensure the output is sorted in descending order
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    output = task_func(df, "col1", "col2")
    assert output == [2, 1, 0]

    # Test case 4: Ensure the output is limited to the specified number of elements
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    output = task_func(df, "col1", "col2", N=2)
    assert len(output) == 2

    # Test case 5: Ensure the output is correct for a larger dataset
    df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [6, 7, 8, 9, 10]})
    output = task_func(df, "col1", "col2")
    assert output == [4, 3, 2, 1, 0]