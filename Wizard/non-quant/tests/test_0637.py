python
import pytest
from src_0637 import task_func

def test_task_func():
    # Test case 1: Non-zero rows
    df, ax = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (10, 5)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert ax.get_xlabel() == 'Column'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_xticks() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels() == COLUMNS
    assert ax.get_ylim() == (0, 10)
    assert ax.get_yticks() == [0, 2, 4, 6, 8, 10]
    assert ax.get_yticklabels() == ['0', '2', '4', '6', '8', '10']
    assert ax.get_legend().get_texts() == []
    assert ax.get_legend().get_title().get_text() == ''
    
    # Test case 2: Zero rows
    df, ax = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (0, 5)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert ax.get_xlabel() == 'Column'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_xticks() == []
    assert ax.get_xticklabels() == []
    assert ax.get_ylim() == (0, 0)
    assert ax.get_yticks() == []
    assert ax.get_yticklabels() == []
    assert ax.get_legend().get_texts() == []
    assert ax.get_legend().get_title().get_text() == ''
    
    # Test case 3: Negative rows
    df, ax = task_func(-10)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (0, 5)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert ax.get_xlabel() == 'Column'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_xticks() == []
    assert ax.get_xticklabels() == []
    assert ax.get_ylim() == (0, 0)
    assert ax.get_yticks() == []
    assert ax.get_yticklabels() == []
    assert ax.get_legend().get_texts() == []
    assert ax.get_legend().get_title().get_text() == ''