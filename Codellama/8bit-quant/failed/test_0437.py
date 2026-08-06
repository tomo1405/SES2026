import pytest
from src_0437 import task_func

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_value_error():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_valid_input():
    letter_counts, ax = task_func("hello world")
    assert letter_counts == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    assert ax.get_xlabel() == "Letters"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Letter Frequencies"