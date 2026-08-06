python
import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import pytest

def task_func(num_rows=5, rand_range=(0, 100)):
    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame({label: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for label in labels})

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    return fig

def test_task_func():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert isinstance(fig.axes[0], plt.Axes)
    assert len(fig.axes[0].patches) == 5
    assert all(isinstance(patch, plt.Rectangle) for patch in fig.axes[0].patches)
    assert all(patch.get_height() > 0 for patch in fig.axes[0].patches)
    assert all(patch.get_width() > 0 for patch in fig.axes[0].patches)
    assert all(patch.get_y() == 0 for patch in fig.axes[0].patches)
    assert all(patch.get_x() == i for i, patch in enumerate(fig.axes[0].patches))
    assert all(patch.get_facecolor() == (0.0, 0.0, 0.0, 0.0) for patch in fig.axes[0].patches)
    assert all(patch.get_edgecolor() == (0.0, 0.0, 0.0, 1.0) for patch in fig.axes[0].patches)
    assert all(patch.get_linewidth() == 0 for patch in fig.axes[0].patches)
    assert all(patch.get_linestyle() == 'None' for patch in fig.axes[0].patches)
    assert all(patch.get_alpha() == 0.5 for patch in fig.axes[0].patches)
    assert all(patch.get_visible() for patch in fig.axes[0].patches)
    assert all(isinstance(label.get_text(), str) for label in fig.axes[0].get_xticklabels())
    assert all(isinstance(label.get_text(), str) for label in fig.axes[0].get_yticklabels())
    assert all(label.get_fontsize() == 10 for label in fig.axes[0].get_xticklabels())
    assert all(label.get_fontsize() == 10 for label in fig.axes[0].get_yticklabels())
    assert all(label.get_color() == (0.0, 0.0, 0.0, 1.0) for label in fig.axes[0].get_xticklabels())
    assert all(label.get_color() == (0.0, 0.0, 0.0, 1.0) for label in fig.axes[0].get_yticklabels())
    assert all(label.get_rotation() == 0 for label in fig.axes[0].get_xticklabels())
    assert all(label.get_rotation() == 0 for label in fig.axes[0].get_yticklabels())
    assert all(label.get_ha() == 'center' for label in fig.axes[0].get_xticklabels())
    assert all(label.get_ha() == 'center' for label in fig.axes[0].get_yticklabels())
    assert all(label.get_va() == 'center' for label in fig.axes[0].get_xticklabels())
    assert all(label.get_va() == 'center' for label in fig.axes[0].get_yticklabels())
    assert all(label.get_visible() for label in fig.axes[0].get_xticklabels())
    assert all(label.get_visible() for label in fig.axes[0].get_yticklabels())
    assert all(isinstance(label.get_text(), str) for label in fig.axes[0].get_legend().get_texts())
    assert all(label.get_fontsize() == 10 for label in fig.axes[0].get_legend().get_texts())
    assert all(label.get_color() == (0.0, 0.0, 0.0, 1.0) for label in fig.axes[0].get_legend().get_texts())
    assert all(label.get_visible() for label in fig.axes[0].get_legend().get_texts())
    assert all(isinstance(line.get_color(), tuple) for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_linewidth() == 1.0 for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_linestyle() == '-' for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_alpha() == 1.0 for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_visible() for line in fig.axes[0].get_legend().get_lines())
    assert all(isinstance(line.get_marker(), str) for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_markersize() == 6.0 for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_markeredgewidth() == 1.0 for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_markeredgecolor() == (0.0, 0.0, 0.0, 1.0) for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_markerfacecolor() == (0.0, 0.0, 0.0, 0.0) for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_markerfacecoloralt() == (0.0, 0.0, 0.0, 0.0) for line in fig.axes[0].get_legend().get_lines())
    assert all(isinstance(line.get_label(), str) for line in fig.axes[0].get_legend().get_lines())
    assert all(line.get_label() in labels for line in fig.axes[0].get_legend().get_lines())