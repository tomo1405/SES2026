import pytest
from src_0125 import task_func

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_input_value():
    with pytest.raises(ValueError):
        task_func([1, 2, 3, 'a'])

def test_task_func_output_type():
    assert isinstance(task_func([1, 2, 3]), tuple)

def test_task_func_output_value():
    assert task_func([1, 2, 3]) == (12, 12)

def test_task_func_random_list():
    random_list = task_func([1, 2, 3])[0]
    assert len(random_list) == 12
    assert all(isinstance(item, int) for item in random_list)
    assert all(item >= 1 and item <= 100 for item in random_list)

def test_task_func_histogram():
    ax = task_func([1, 2, 3])[1]
    assert ax.get_title() == 'Histogram of Random Numbers'
    assert ax.get_xlabel() == 'Number'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (1, 100)
    assert ax.get_ylim() == (0, 12)
    assert ax.get_xticks() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]