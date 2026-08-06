python
import pytest
from src_0164 import task_func

def test_task_func():
    # Test case 1: Default values
    ax = task_func()
    assert ax is not None
    assert ax.get_xlabel() == 'A'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Stacked Bar Chart'

    # Test case 2: Custom values
    ax = task_func(rows=10, cols=3)
    assert ax is not None
    assert ax.get_xlabel() == 'C'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Stacked Bar Chart'

    # Test case 3: Invalid number of columns
    with pytest.raises(ValueError):
        task_func(rows=5, cols=6)