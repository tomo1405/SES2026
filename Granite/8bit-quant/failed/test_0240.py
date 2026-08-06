import pytest
from src_0240 import task_func

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]  # Replace this with your own input data
    arr, computed_stats, ax = task_func(original)
    
    # Test the return value of the function
    assert isinstance(arr, np.ndarray)
    assert isinstance(computed_stats, dict)
    assert isinstance(ax, plt.Axes)
    
    # Test the computed statistics
    assert computed_stats['mean'] == pytest.approx(3.5)  # Replace this with the expected mean value
    assert computed_stats['std'] == pytest.approx(1.707825127659933)  # Replace this with the expected standard deviation value
    assert computed_stats['min'] == 2
    assert computed_stats['max'] == 6
    
    # Test the plot
    assert ax.get_title() == 'Histogram with PDF'
    assert ax.get_legend_handles_labels() == ([<matplotlib.legend.Legend object at 0x7f815d40c1d0>], ['Histogram', 'PDF'])