import pytest
from src_1033 import task_func

def test_task_func():
    # Test case 1: Check if the function returns None when the DataFrame is empty
    with pytest.warns(UserWarning, match="No data to generate heatmap."):
        result = task_func(rows=0)
        assert result is None

    # Test case 2: Check if the function returns a heatmap when the DataFrame is not empty
    result = task_func(rows=1000, string_length=3)
    assert result is not None
    assert result.get_figure() is not None