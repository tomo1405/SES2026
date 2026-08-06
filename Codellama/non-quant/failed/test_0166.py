import pytest
from src_0166 import task_func

def test_task_func():
    num_rows = 5
    rand_range = (0, 100)
    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame({label: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for label in labels})

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.get_xticklabels()) == len(labels)
    assert len(ax.get_yticklabels()) == len(labels)
    assert all(label in ax.get_xticklabels() for label in labels)
    assert all(label in ax.get_yticklabels() for label in labels)