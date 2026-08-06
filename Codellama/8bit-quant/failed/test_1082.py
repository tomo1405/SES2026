import pytest
from src_1082 import task_func

def test_task_func_with_valid_data():
    data = {
        "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
        "Height": [160, 165, 170, 175, 180],
    }
    ax = task_func(data)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Weight vs Height"
    assert ax.get_xlabel() == "Weight_Float"
    assert ax.get_ylabel() == "Height"

def test_task_func_with_invalid_data():
    data = {
        "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
        "Height": [160, 165, 170, 175, 180],
    }
    with pytest.raises(ValueError):
        task_func(data)