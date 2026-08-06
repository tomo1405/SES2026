python
import pytest
from src_0474 import task_func

def test_task_func():
    # Test valid inputs
    ax = task_func(n_walks=2, n_steps=10, seed=42)
    assert isinstance(ax, plt.Axes)
    assert ax.get_xlabel() == "Step"
    assert ax.get_ylabel() == "Position"
    assert ax.get_title() == "Random walks"
    assert len(ax.lines) == 2
    assert ax.lines[0].get_data()[0].shape == (10,)
    assert ax.lines[1].get_data()[0].shape == (10,)
    assert ax.lines[0].get_color() == "b"
    assert ax.lines[1].get_color() == "g"
    
    # Test invalid inputs
    with pytest.raises(ValueError):
        task_func(n_walks=-1, n_steps=10)
    with pytest.raises(ValueError):
        task_func(n_walks=1, n_steps=-1)