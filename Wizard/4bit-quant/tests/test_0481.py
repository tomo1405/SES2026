python
import pytest
from src_0481 import task_func

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, grape, lemon", "peach, plum, cherry"]
    df = task_func(data_list)
    assert df.shape == (3, 2)
    assert df.iloc[0]["Original String"] == "apple, banana, cherry"
    assert df.iloc[0]["Shuffled String"] == "cherry, banana, apple"
    assert df.iloc[1]["Original String"] == "orange, grape, lemon"
    assert df.iloc[1]["Shuffled String"] == "lemon, grape, orange"
    assert df.iloc[2]["Original String"] == "peach, plum, cherry"
    assert df.iloc[2]["Shuffled String"] == "cherry, plum, peach"