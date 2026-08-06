import pytest
from src_0513 import task_func


def test_task_func():
    data = [
        ["Product A", 10, 100],
        ["Product B", 5, 50],
        ["Product C", 20, 200]
    ]
    column = "Quantity Sold"
    expected_result = {
        "sum": 35,
        "mean": 11.666666666666666,
        "min": 5,
        "max": 20
    }
    expected_ax_title = "Bar Chart of Quantity Sold"

    result, ax = task_func(column, data)

    assert result == expected_result
    assert ax.get_title() == expected_ax_title

def test_task_func_with_negative_values():
    data = [
        ["Product A", 10, 100],
        ["Product B", -5, 50],
        ["Product C", 20, 200]
    ]
    column = "Quantity Sold"

    with pytest.raises(ValueError) as e:
        task_func(column, data)

    assert str(e.value) == "Value must not be negative"