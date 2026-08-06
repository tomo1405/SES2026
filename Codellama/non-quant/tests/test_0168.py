import pandas as pd
from src_0168 import task_func


def test_task_func():
    num_types = 5
    integer_range = (0, 100)
    LABELS = [f'Type{i + 1}' for i in range(num_types)]
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in LABELS})

    fig, ax = task_func(num_types, integer_range)

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.get_xticklabels()) == num_types
    assert len(ax.get_yticklabels()) == num_types
    assert all(label in ax.get_xticklabels() for label in LABELS)
    assert all(label in ax.get_yticklabels() for label in LABELS)