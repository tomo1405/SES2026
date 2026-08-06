import pytest
from src_1059 import task_func

def test_task_func():
    # Test with default value
    ax = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Countplot"
    assert ax.get_xlabel() == "Shape:Color"
    assert ax.get_ylabel() == "Count"
    assert ax.get_legend() == None
    assert ax.get_xticks() == SHAPES
    assert ax.get_yticks() == COLORS
    assert ax.get_xticklabels() == SHAPES
    assert ax.get_yticklabels() == COLORS
    assert ax.get_xticklabels_rotation() == 90
    assert ax.get_palette() == "Set3"

    # Test with custom value
    ax = task_func(num_pairs=5)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Countplot"
    assert ax.get_xlabel() == "Shape:Color"
    assert ax.get_ylabel() == "Count"
    assert ax.get_legend() == None
    assert ax.get_xticks() == SHAPES[:5]
    assert ax.get_yticks() == COLORS[:5]
    assert ax.get_xticklabels() == SHAPES[:5]
    assert ax.get_yticklabels() == COLORS[:5]
    assert ax.get_xticklabels_rotation() == 90
    assert ax.get_palette() == "Set3"