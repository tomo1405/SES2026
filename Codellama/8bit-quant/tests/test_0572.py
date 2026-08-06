import pandas as pd
import pytest
from src_0572 import task_func


def test_task_func_valid_input():
    f_list = [lambda x: x, lambda y: y]
    file_path = "test_output.csv"
    task_func(f_list, file_path)
    df = pd.read_csv(file_path)
    assert df.shape == (2, 5)
    assert df["Function Name"].tolist() == ["<lambda>", "<lambda>"]
    assert df["Number of Arguments"].tolist() == [1, 1]
    assert df["Defaults"].tolist() == [None, None]
    assert df["Annotations"].tolist() == [None, None]
    assert df["Is Lambda"].tolist() == [True, True]

def test_task_func_invalid_input():
    f_list = [lambda x: x, lambda y: y]
    file_path = 123
    with pytest.raises(ValueError):
        task_func(f_list, file_path)

def test_task_func_empty_list():
    f_list = []
    file_path = "test_output.csv"
    with pytest.raises(ValueError):
        task_func(f_list, file_path)

def test_task_func_non_callable_element():
    f_list = [lambda x: x, 123]
    file_path = "test_output.csv"
    with pytest.raises(ValueError):
        task_func(f_list, file_path)