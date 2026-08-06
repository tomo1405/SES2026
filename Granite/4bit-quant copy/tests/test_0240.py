import pytest
from src_0240 import task_func

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]  # Replace with your own test data
    arr, computed_stats, ax = task_func(original)
    
    # Test the return value of the function
    assert isinstance(arr, np.ndarray)
    assert isinstance(computed_stats, dict)
    assert isinstance(ax, plt.Axes)
    
    # Test the computed statistics
    assert computed_stats['mean'] == pytest.approx(3.3333333333333335)
    assert computed_stats['std'] == pytest.approx(1.8708286933869707)
    assert computed_stats['min'] == 1
    assert computed_stats['max'] == 6
    
    # Test the plot
    assert ax.get_title() == 'Histogram with PDF'
    assert ax.get_legend_handles_labels() == ([<matplotlib.legend.Legend object at 0x7f225e91c400>], ['Histogram', 'PDF'])