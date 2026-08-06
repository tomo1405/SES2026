import pytest
from src_1059 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_xlabel() == "Pairs"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Pair Counts"

def test_task_func_with_num_pairs():
    ax = task_func(num_pairs=5)
    assert ax is not None
    assert len(ax.patches) == 5

def test_task_func_with_invalid_num_pairs():
    with pytest.raises(ValueError):
        task_func(num_pairs=-1)