import pytest
from src_0209 import task_func

def test_task_func():
    elements = 100
    seed = 0
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert ax is not None
    assert len(descriptive_stats) == 5
    assert descriptive_stats['50%'] == 0
    assert ax.get_title() == 'Random Walk'