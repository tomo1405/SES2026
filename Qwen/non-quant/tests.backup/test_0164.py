import pytest
from src_0164 import task_func

def test_task_func_default_parameters():
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_ylabel() == 'Value'
    assert list(ax.get_legend().get_texts()) == ['A', 'B', 'C', 'D', 'E']

def test_task_func_custom_rows_and_cols():
    ax = task_func(rows=3, cols=3)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_ylabel() == 'Value'
    assert list(ax.get_legend().get_texts()) == ['A', 'B', 'C']

def test_task_func_max_columns():
    ax = task_func(cols=5)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_ylabel() == 'Value'
    assert list(ax.get_legend().get_texts()) == ['A', 'B', 'C', 'D', 'E']

def test_task_func_invalid_columns():
    with pytest.raises(ValueError) as excinfo:
        task_func(cols=6)
    assert str(excinfo.value) == "Maximum number of columns allowed is 5"