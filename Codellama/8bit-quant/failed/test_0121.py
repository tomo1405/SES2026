import pytest
from src_0121 import task_func

def test_task_func_valid_input():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    expected_output = pd.Series([datetime(2020, 1, 1), datetime(2020, 12, 31)])
    assert task_func(start_date, end_date, seed) == expected_output

def test_task_func_invalid_input():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    with pytest.raises(ValueError):
        task_func(start_date, end_date, seed)

def test_task_func_invalid_input_2():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    with pytest.raises(ValueError):
        task_func(start_date, end_date, seed)

def test_task_func_invalid_input_3():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    seed = 42
    with pytest.raises(ValueError):
        task_func(start_date, end_date, seed)