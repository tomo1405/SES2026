import pytest
from src_0400 import task_func

def test_task_func():
    # Test case 1: Positive frequency, positive sample size
    frequency = 10
    sample_size = 1000
    fig, ax = task_func(frequency, sample_size)
    assert fig is not None
    assert ax is not None
    assert len(ax.lines) == 2
    assert ax.lines[0].get_label() == 'sin'
    assert ax.lines[1].get_label() == 'cos'

    # Test case 2: Positive frequency, negative sample size
    frequency = 10
    sample_size = -1000
    with pytest.raises(ValueError):
        task_func(frequency, sample_size)

    # Test case 3: Negative frequency, positive sample size
    frequency = -10
    sample_size = 1000
    with pytest.raises(ValueError):
        task_func(frequency, sample_size)

    # Test case 4: Negative frequency, negative sample size
    frequency = -10
    sample_size = -1000
    with pytest.raises(ValueError):
        task_func(frequency, sample_size)