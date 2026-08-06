python
import pytest
from src_0637 import task_func

def test_task_func():
    # Test case 1: Non-zero rows
    df, ax = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (5, 5)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert ax.get_xlabel() == 'Column'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_xticks() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels() == COLUMNS
    assert ax.get_ylim() == (0, 5)
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5]
    assert ax.get_yticklabels() == [0, 1, 2, 3, 4, 5]
    assert ax.get_legend().get_texts() == []
    assert ax.get_legend().get_title().get_text() == ''
    assert ax.get_legend().get_visible() == False
    
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
    assert ax.get_legend().get_visible() == False
    
    # Test case 3: Negative rows
    df, ax = task_func(-1)
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
    assert ax.get_legend().get_visible() == False