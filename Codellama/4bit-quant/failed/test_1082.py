import pytest
from src_1082 import task_func

def test_task_func():
    # Test 1: Validate that the function raises an error when weights are not strings
    data = {
        "Weight_String": [60.5, 65.7, 70.2, 75.9, 80.1],
        "Height": [160, 165, 170, 175, 180],
    }
    with pytest.raises(ValueError):
        task_func(data)

    # Test 2: Validate that the function converts string weights to floats
    data = {
        "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
        "Height": [160, 165, 170, 175, 180],
    }
    df = task_func(data)
    assert all(isinstance(weight, float) for weight in df["Weight_Float"])

    # Test 3: Validate that the function plots the scatter plot correctly
    data = {
        "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
        "Height": [160, 165, 170, 175, 180],
    }
    ax = task_func(data)
    assert ax.get_title() == "Weight vs Height"
    assert ax.get_xlabel() == "Weight"
    assert ax.get_ylabel() == "Height"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_xdata() == [60.5, 65.7, 70.2, 75.9, 80.1]
    assert ax.get_lines()[0].get_ydata() == [160, 165, 170, 175, 180]