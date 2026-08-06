import pytest
from src_1044 import task_func

def test_task_func_empty_data_list():
    with pytest.raises(ValueError):
        task_func([])

def test_task_func_non_empty_data_list():
    data_list = [1, 2, 3, 4, 5]
    ax = task_func(data_list)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xticks() == CATEGORIES
    assert ax.get_xticklabels() == CATEGORIES
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_yticklabels() == [0, 1, 2, 3, 4, 5]

def test_task_func_predefined_categories():
    data_list = [1, 2, 3, 4, 5]
    ax = task_func(data_list)
    assert ax.get_xticks() == CATEGORIES
    assert ax.get_xticklabels() == CATEGORIES
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_yticklabels() == [0, 1, 2, 3, 4, 5]

def test_task_func_extra_categories():
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ax = task_func(data_list)
    assert ax.get_xticks() == CATEGORIES + ["F"]
    assert ax.get_xticklabels() == CATEGORIES + ["F"]
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ax.get_yticklabels() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]