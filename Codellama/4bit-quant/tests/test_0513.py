import pytest
from src_0513 import task_func

def test_task_func():
    # Test case 1: Test with valid data
    data = [
        ["Product A", 10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300]
    ]
    result, ax = task_func("Quantity Sold", data)
    assert result["sum"] == 60
    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30
    assert ax.title.get_text() == "Bar Chart of Quantity Sold"

    # Test case 2: Test with invalid data
    data = [
        ["Product A", -10, 100],
        ["Product B", 20, 200],
        ["Product C", 30, 300]
    ]
    with pytest.raises(ValueError):
        task_func("Quantity Sold", data)

    data = [
        ["Product A", 10, -100],
        ["Product B", 20, 200],
        ["Product C", 30, 300]
    ]
    with pytest.raises(ValueError):
        task_func("Total Sales", data)