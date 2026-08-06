from io import StringIO
from unittest.mock import patch

import pytest
from src_1044 import task_func


def test_task_func_with_empty_data_list():
    with patch("sys.stdout", new=StringIO()) as fake_stdout:
        with pytest.raises(ValueError) as exc_info:
            task_func([])
        assert "The data list is empty." in str(exc_info.value)
    assert fake_stdout.getvalue() == ""

def test_task_func_with_uniform_distribution():
    data_list = ["A", "B", "C", "D", "E"] * 10
    ax = task_func(data_list)
    assert ax is not None
    # You can add more assertions to check the output of the function

def test_task_func_with_non_uniform_distribution():
    data_list = ["A", "B", "C", "D", "E"] * 10 + ["A"] * 1
    ax = task_func(data_list)
    assert ax is not None
    # You can add more assertions to check the output of the function

def test_task_func_with_extra_categories():
    data_list = ["A", "B", "C", "D", "E"] * 10 + ["F", "G"] * 1
    ax = task_func(data_list)
    assert ax is not None
    # You can add more assertions to check the output of the function