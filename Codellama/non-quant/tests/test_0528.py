import pytest
from src_0528 import task_func

def test_task_func():
    input_file = "test_data.json"
    results, ax = task_func(input_file)
    assert isinstance(results, dict)
    assert isinstance(ax, plt.Axes)
    assert all(isinstance(key, str) for key in results.keys())
    assert all(isinstance(value, dict) for value in results.values())
    assert all(isinstance(mean, float) for mean in results.values())
    assert all(isinstance(median, float) for median in results.values())
    assert all(isinstance(key, str) for key in ax.get_xticklabels())
    assert all(isinstance(value, float) for value in ax.get_yticklabels())
    assert ax.get_title() == "Boxplot of Values for Each Key"