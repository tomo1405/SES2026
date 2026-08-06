import pytest
from src_0525 import task_func

def test_task_func():
    # Test case 1: empty input
    with pytest.raises(ValueError):
        task_func([])

    # Test case 2: input is not a list of dictionaries
    with pytest.raises(TypeError):
        task_func(123)

    # Test case 3: input is a list of dictionaries, but not all values are numeric
    with pytest.raises(TypeError):
        task_func([{"a": 1, "b": 2}, {"a": "hello", "b": 2}])

    # Test case 4: valid input
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    result, axes = task_func(data)
    assert isinstance(result, dict)
    assert isinstance(axes, list)
    assert len(axes) == 2
    assert axes[0].get_title() == "Statistics of a"
    assert axes[1].get_title() == "Statistics of b"
    assert axes[0].get_ylabel() == "Value"
    assert axes[1].get_ylabel() == "Value"
    assert axes[0].get_xlabel() == "mean"
    assert axes[1].get_xlabel() == "std"
    assert axes[0].get_xticks() == ["mean", "std"]
    assert axes[1].get_xticks() == ["mean", "std"]
    assert axes[0].get_yticks() == [1, 3]
    assert axes[1].get_yticks() == [2, 4]