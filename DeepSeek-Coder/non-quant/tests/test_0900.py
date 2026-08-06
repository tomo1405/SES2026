import pytest
from src_0900 import task_func

def test_task_func():
    # Test basic functionality
    result = task_func()
    assert len(result) == 10000
    assert result[0] == 0  # Starting at 0
    assert result[-1] == 0  # Should end at 0 due to equal probability of 1 and -1

    # Test with specific seed
    result_seed = task_func(seed=12345)
    assert result_seed != result  # Ensure different seed produces different results

    # Test with negative length
    with pytest.raises(ValueError):
        task_func(length=-1)