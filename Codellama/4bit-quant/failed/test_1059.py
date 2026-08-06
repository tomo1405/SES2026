import pytest
from src_1059 import task_func

def test_task_func():
    # Test with default arguments
    ax = task_func()
    assert ax.get_title() == "Countplot"
    assert ax.get_xlabel() == "Shape:Color"
    assert ax.get_ylabel() == "Count"
    assert ax.get_legend() == False
    assert ax.get_xticks() == SHAPES
    assert ax.get_yticks() == COLORS
    assert ax.get_palette() == "Set3"

    # Test with custom arguments
    ax = task_func(num_pairs=5)
    assert ax.get_title() == "Countplot"
    assert ax.get_xlabel() == "Shape:Color"
    assert ax.get_ylabel() == "Count"
    assert ax.get_legend() == False
    assert ax.get_xticks() == SHAPES[:5]
    assert ax.get_yticks() == COLORS[:5]
    assert ax.get_palette() == "Set3"

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(num_pairs=0)
        task_func(num_pairs=-1)
        task_func(num_pairs=1000)