import pytest
from src_0517 import task_func

def test_task_func_valid_input():
    array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    df, results = task_func(array)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(results, sm.regression.linear_model.RegressionResultsWrapper)
    assert list(df.columns) == ["A", "B", "C", "D", "Response"]

def test_task_func_invalid_row_length():
    array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9],  # Invalid row length
        [11, 12, 13, 14, 15]
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func(array)
    assert str(excinfo.value) == "Each sub-list in the input 2D list must have exactly 5 elements."

def test_task_func_empty_input():
    array = []
    with pytest.raises(ValueError) as excinfo:
        task_func(array)
    assert str(excinfo.value) == "Each sub-list in the input 2D list must have exactly 5 elements."

def test_task_func_random_seed_consistency():
    array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    df1, results1 = task_func(array, random_seed=0)
    df2, results2 = task_func(array, random_seed=0)
    assert df1.equals(df2)
    assert results1.summary() == results2.summary()