import pytest
from src_0435 import task_func

def test_task_func_valid_input():
    s = "1234567890\n1234567890\n1234567890\n1234567890\n1234567890"
    seed = 0
    df = task_func(s, seed)
    assert df.shape == (5, 6)
    assert df.columns.tolist() == ["ID", "Quantity", "Code", "Price", "Product", "Description"]
    assert df["Quantity"].dtype == int
    assert df["Price"].dtype == int

def test_task_func_invalid_input():
    s = ""
    seed = 0
    with pytest.raises(ValueError):
        task_func(s, seed)

def test_task_func_invalid_input_2():
    s = "1234567890\n1234567890\n1234567890\n1234567890\n1234567890"
    seed = 0
    with pytest.raises(ValueError):
        task_func(s, seed)

def test_task_func_invalid_input_3():
    s = "1234567890\n1234567890\n1234567890\n1234567890\n1234567890"
    seed = 0
    with pytest.raises(ValueError):
        task_func(s, seed)

def test_task_func_invalid_input_4():
    s = "1234567890\n1234567890\n1234567890\n1234567890\n1234567890"
    seed = 0
    with pytest.raises(ValueError):
        task_func(s, seed)

def test_task_func_invalid_input_5():
    s = "1234567890\n1234567890\n1234567890\n1234567890\n1234567890"
    seed = 0
    with pytest.raises(ValueError):
        task_func(s, seed)