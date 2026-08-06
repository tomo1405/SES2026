import pytest
from src_0225 import task_func

def test_task_func():
    # Test case 1: range_start < range_end
    data, ax, mean, median = task_func(range_start=-10, range_end=10, step=0.1)
    assert data is not None
    assert ax is not None
    assert mean is not None
    assert median is not None

    # Test case 2: range_start > range_end
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=-10, step=0.1)

    # Test case 3: step is not a number
    with pytest.raises(TypeError):
        task_func(range_start=-10, range_end=10, step='0.1')

    # Test case 4: range_start is not a number
    with pytest.raises(TypeError):
        task_func(range_start='-10', range_end=10, step=0.1)

    # Test case 5: range_end is not a number
    with pytest.raises(TypeError):
        task_func(range_start=-10, range_end='10', step=0.1)

    # Test case 6: step is negative
    with pytest.raises(ValueError):
        task_func(range_start=-10, range_end=10, step=-0.1)

    # Test case 7: range_start is negative
    with pytest.raises(ValueError):
        task_func(range_start=-10, range_end=10, step=0.1)

    # Test case 8: range_end is negative
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=-10, step=0.1)

    # Test case 9: step is zero
    with pytest.raises(ValueError):
        task_func(range_start=-10, range_end=10, step=0)

    # Test case 10: range_start is zero
    with pytest.raises(ValueError):
        task_func(range_start=0, range_end=10, step=0.1)

    # Test case 11: range_end is zero
    with pytest.raises(ValueError):
        task_func(range_start=-10, range_end=0, step=0.1)