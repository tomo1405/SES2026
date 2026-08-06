import pandas as pd


def test_task_func():
    num_rows = 5
    rand_range = (0, 100)
    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame({label: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for label in labels})

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(fig.axes) == 1
    assert len(ax.patches) == len(labels)
    assert all(isinstance(patch, mpl.patches.Patch) for patch in ax.patches)
    assert all(patch.get_label() in labels for patch in ax.patches)
    assert all(patch.get_height() >= 0 for patch in ax.patches)
    assert all(patch.get_height() <= rand_range[1] for patch in ax.patches)