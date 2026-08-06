import pytest
from src_0165 import task_func

def test_task_func():
    # Test that the function returns a matplotlib figure
    fig = task_func()
    assert isinstance(fig, plt.Figure)

    # Test that the figure has the correct number of axes
    assert len(fig.axes) == 1

    # Test that the figure has the correct number of labels
    assert len(fig.axes[0].get_xticklabels()) == 5

    # Test that the figure has the correct data range
    assert np.allclose(fig.axes[0].get_xlim(), (0, 1))

    # Test that the figure has the correct data range
    assert np.allclose(fig.axes[0].get_ylim(), (0, 1))

    # Test that the figure has the correct data range
    assert np.allclose(fig.axes[0].get_zlim(), (0, 1))

    # Test that the figure has the correct data range
    assert np.allclose(fig.axes[0].get_xlabel(), 'Label1')

    # Test that the figure has the correct data range
    assert np.allclose(fig.axes[0].get_ylabel(), 'Label2')

    # Test that the figure has the correct data range
    assert np.allclose(fig.axes[0].get_zlabel(), 'Label3')

    # Test that the figure has the correct data range
    assert np.allclose(fig.axes[0].get_title(), 'Stacked Bar Chart')