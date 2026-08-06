import pytest
from src_0100 import task_func

def test_task_func():
    fig = task_func()
    
    # Check if the figure is created
    assert isinstance(fig, plt.Figure), "The returned object should be a matplotlib Figure"
    
    # Check if the title is set correctly
    assert fig.axes[0].get_title() == 'Iris Dataset Pair Plot', "The figure title should be 'Iris Dataset Pair Plot'"
    
    # Check if there are 6 axes (2x3 grid for pair plot)
    assert len(fig.axes) == 6, "There should be 6 axes in the figure (2x3 grid)"
    
    # Check if each axis has the correct number of lines (should be 3 lines per axis for 3 species)
    for ax in fig.axes:
        assert len(ax.get_lines()) == 3, "Each axis should have 3 lines (one for each species)"