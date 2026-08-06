import pytest
from src_0561 import task_func

def test_task_func():
    # Test with valid data
    data = "2022-01-10,2022-02-20,2022-03-30"
    ax = task_func(data)
    assert ax.get_xlabel() == "Month"
    assert ax.get_ylabel() == "Value"
    assert ax.get_title() == "Monthly Data for 2022"
    assert ax.get_xticks() == ["January", "February", "March"]
    assert ax.get_yticks() == [10, 20, 30]

    # Test with invalid data
    data = ""
    with pytest.raises(ValueError):
        task_func(data)

    data = "2022-01-10,2022-02-20,2022-03-30,2023-01-10"
    with pytest.raises(ValueError):
        task_func(data)