import pytest
from src_0125 import task_func
import matplotlib.pyplot as plt

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_input_elements_type():
    with pytest.raises(ValueError):
        task_func([1, "not a number", 3])

def test_task_func_output_type():
    result = task_func([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], plt.Axes)

def test_task_func_random_list_length():
    result = task_func([1, 2, 3], size=5)
    _, ax = result
    random_list, _ = ax.get_lines()[0].get_data()
    assert len(random_list) <= 5

def test_task_func_random_list_values():
    result = task_func([1, 2, 3], size=5)
    _, ax = result
    random_list, _ = ax.get_lines()[0].get_data()
    assert all(1 <= num <= 100 for num in random_list)

def test_task_func_histogram_title():
    result = task_func([1, 2, 3])
    _, ax = result
    assert ax.get_title() == 'Histogram of Random Numbers'

def test_task_func_histogram_labels():
    result = task_func([1, 2, 3])
    _, ax = result
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'

def test_task_func_execution_time():
    result = task_func([1, 2, 3])
    execution_time, _ = result
    assert execution_time >= 0

def test_task_func_with_large_list():
    large_list = list(range(1000))
    result = task_func(large_list, size=500)
    _, ax = result
    random_list, _ = ax.get_lines()[0].get_data()
    assert len(random_list) <= 500

def test_task_func_with_zero_size():
    result = task_func([1, 2, 3], size=0)
    _, ax = result
    random_list, _ = ax.get_lines()[0].get_data()
    assert len(random_list) == 0

def test_task_func_with_negative_size():
    result = task_func([1, 2, 3], size=-10)
    _, ax = result
    random_list, _ = ax.get_lines()[0].get_data()
    assert len(random_list) == 0

def test_task_func_with_seed():
    result1 = task_func([1, 2, 3], seed=42)
    result2 = task_func([1, 2, 3], seed=42)
    assert result1 == result2