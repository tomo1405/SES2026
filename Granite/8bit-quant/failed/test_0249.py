import pytest
from src_0249 import task_func

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(data_list)
    assert ax is not None
    assert ax.get_legend_handles_labels() == ([<matplotlib.legend.Legend object at 0x7f8e1d1d0b00>], ['Position 1', 'Position 2', 'Position 3'])

def test_task_func_empty_data_list():
    data_list = [[]]
    with pytest.raises(ValueError) as excinfo:
        task_func(data_list)
    assert 'Empty data_list' in str(excinfo.value)