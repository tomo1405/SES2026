import pytest
from src_0895 import task_func

def test_task_func():
    array, mean, std, ax = task_func()
    
    # Test that the array has the correct size
    assert len(array) == ARRAY_SIZE
    
    # Test that the mean and standard deviation are calculated correctly
    assert mean == pytest.approx(np.mean(array))
    assert std == pytest.approx(np.std(array))
    
    # Test that the histogram plot is created correctly
    assert ax.get_title() == 'Histogram of Random Integers'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.lines[0].get_color() == 'red'
    assert ax.lines[0].get_linestyle() == 'dashed'
    assert ax.lines[0].get_linewidth() == 1
    assert ax.lines[1].get_color() == 'purple'
    assert ax.lines[1].get_linestyle() == 'dashed'
    assert ax.lines[1].get_linewidth() == 1
    assert ax.lines[2].get_color() == 'purple'
    assert ax.lines[2].get_linestyle() == 'dashed'
    assert ax.lines[2].get_linewidth() == 1
    assert ax.legend().get_texts()[0].get_text() == 'Mean'
    assert ax.legend().get_texts()[1].get_text() == 'Standard Deviation'