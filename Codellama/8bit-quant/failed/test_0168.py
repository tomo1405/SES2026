import pytest
from src_0168 import task_func

def test_task_func():
    num_types = 5
    integer_range = (0, 100)
    LABELS = [f'Type{i + 1}' for i in range(num_types)]
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in LABELS})

    fig, ax = task_func(num_types, integer_range)

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == num_types
    assert all(isinstance(patch, mpl.patches.Patch) for patch in ax.patches)
    assert all(patch.get_height() >= 0 for patch in ax.patches)
    assert all(patch.get_width() >= 0 for patch in ax.patches)
    assert all(patch.get_x() >= 0 for patch in ax.patches)
    assert all(patch.get_y() >= 0 for patch in ax.patches)
    assert all(patch.get_label() in LABELS for patch in ax.patches)