import pytest
from src_0197 import task_func

def test_task_func():
    # Test with default parameters
    plot, numbers = task_func(10)
    assert isinstance(plot, plt.Axes)
    assert len(numbers) == 10
    assert all(1 <= num <= 100 for num in numbers)

    # Test with different parameters
    plot, numbers = task_func(20, range_limit=50)
    assert isinstance(plot, plt.Axes)
    assert len(numbers) == 20
    assert all(1 <= num <= 50 for num in numbers)

    # Test with invalid range_limit
    with pytest.raises(ValueError):
        task_func(10, range_limit=0)