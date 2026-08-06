import matplotlib.pyplot as plt
from src_1070 import task_func


def test_task_func_uniform_distribution():
    data_dict = {
        'A': [1, 2, 3, 4],
        'B': [5, 5, 5, 5]
    }
    axes_list = task_func(data_dict)
    assert len(axes_list) == 2
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

def test_task_func_non_uniform_distribution(capsys):
    data_dict = {
        'A': [1, 1, 2, 2, 3],
        'B': [4, 4, 4, 5, 5]
    }
    axes_list = task_func(data_dict)
    captured = capsys.readouterr()
    assert "The distribution of values in column 'A' is not uniform." in captured.out
    assert "The distribution of values in column 'B' is not uniform." in captured.out
    assert len(axes_list) == 2
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

def test_task_func_empty_data():
    data_dict = {}
    axes_list = task_func(data_dict)
    assert len(axes_list) == 0

def test_task_func_single_column_uniform():
    data_dict = {
        'A': [1, 1, 1, 1]
    }
    axes_list = task_func(data_dict)
    assert len(axes_list) == 1
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

def test_task_func_single_column_non_uniform(capsys):
    data_dict = {
        'A': [1, 2, 3, 4]
    }
    axes_list = task_func(data_dict)
    captured = capsys.readouterr()
    assert "The distribution of values in column 'A' is not uniform." in captured.out
    assert len(axes_list) == 1
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)