import pytest
from src_0834 import task_func

def test_task_func():
    # Test with default arguments
    result = task_func()
    assert result[0] == 5
    assert result[1] == [(5, 200), (6, 190), (7, 180), (8, 170), (9, 160)]

    # Test with custom arguments
    result = task_func(list_length=500, range_start=1, range_end=10, random_seed=42)
    assert result[0] == 5
    assert result[1] == [(5, 250), (6, 240), (7, 230), (8, 220), (9, 210)]

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(list_length=-10, range_start=1, range_end=10, random_seed=42)
    with pytest.raises(ValueError):
        task_func(list_length=1000, range_start=-1, range_end=10, random_seed=42)
    with pytest.raises(ValueError):
        task_func(list_length=1000, range_start=1, range_end=-10, random_seed=42)
    with pytest.raises(ValueError):
        task_func(list_length=1000, range_start=1, range_end=10, random_seed=-42)