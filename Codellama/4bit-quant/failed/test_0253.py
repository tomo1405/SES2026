import pytest
from src_0253 import task_func

@pytest.mark.parametrize("data, labels, expected_colors", [
    ([[1, 2, 3], [4, 5, 6]], ["Series 1", "Series 2"], ["red", "green", "blue"]),
    ([[1, 2, 3], [4, 5, 6]], ["Series 1", "Series 2"], ["red", "green", "blue"]),
    ([[1, 2, 3], [4, 5, 6]], ["Series 1", "Series 2"], ["red", "green", "blue"]),
])
def test_task_func(data, labels, expected_colors):
    ax = task_func(data, labels)
    assert ax.get_legend_handles_labels() == (expected_colors, labels)