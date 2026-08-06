import pytest
from src_1037 import task_func

def test_task_func():
    # Test case 1: intersection is empty
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    ax, intersection_len = task_func(s1, s2)
    assert intersection_len == 0
    assert ax.get_title() == f"Overlap Between {s1.name} and {s2.name}"
    assert ax.get_xlabel() == s1.name
    assert ax.get_ylabel() == "Type"
    assert ax.get_legend() == None
    assert ax.get_xlim() == (0, 6)
    assert ax.get_ylim() == (0, 2)
    assert ax.get_xticks() == [1, 2, 3, 4, 5, 6]
    assert ax.get_yticks() == ["Series1", "Series2"]
    assert ax.get_xticklabels() == [1, 2, 3, 4, 5, 6]
    assert ax.get_yticklabels() == ["Series1", "Series2"]
    assert ax.get_lines() == []

    # Test case 2: intersection is not empty
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([2, 3, 4])
    ax, intersection_len = task_func(s1, s2)
    assert intersection_len == 2
    assert ax.get_title() == f"Overlap Between {s1.name} and {s2.name}"
    assert ax.get_xlabel() == s1.name
    assert ax.get_ylabel() == "Type"
    assert ax.get_legend() == None
    assert ax.get_xlim() == (0, 6)
    assert ax.get_ylim() == (0, 2)
    assert ax.get_xticks() == [1, 2, 3, 4, 5, 6]
    assert ax.get_yticks() == ["Series1", "Series2"]
    assert ax.get_xticklabels() == [1, 2, 3, 4, 5, 6]
    assert ax.get_yticklabels() == ["Series1", "Series2"]
    assert ax.get_lines() == [Line2D(xdata=[2, 3], ydata=[1, 1], color="red", linestyle="--")]

    # Test case 3: intersection is not empty, but series names are different
    s1 = pd.Series([1, 2, 3], name="s1")
    s2 = pd.Series([2, 3, 4], name="s2")
    ax, intersection_len = task_func(s1, s2)
    assert intersection_len == 2
    assert ax.get_title() == f"Overlap Between s1 and s2"
    assert ax.get_xlabel() == s1.name
    assert ax.get_ylabel() == "Type"
    assert ax.get_legend() == None
    assert ax.get_xlim() == (0, 6)
    assert ax.get_ylim() == (0, 2)
    assert ax.get_xticks() == [1, 2, 3, 4, 5, 6]
    assert ax.get_yticks() == ["Series1", "Series2"]
    assert ax.get_xticklabels() == [1, 2, 3, 4, 5, 6]
    assert ax.get_yticklabels() == ["Series1", "Series2"]
    assert ax.get_lines() == [Line2D(xdata=[2, 3], ydata=[1, 1], color="red", linestyle="--")]