python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pytest

def task_func(num_labels=5, data_range=(0, 1)):
    np.random.seed(0)
    columns = [f'Label{i + 1}' for i in range(num_labels)]
    data = pd.DataFrame(np.random.uniform(data_range[0], data_range[1], size=(num_labels, num_labels)), columns=columns)

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    return fig

def test_task_func():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    assert len(fig.axes) == 1
    assert isinstance(fig.axes[0], plt.Axes)
    assert len(fig.axes[0].patches) == 5
    assert all(isinstance(p, plt.Rectangle) for p in fig.axes[0].patches)
    assert all(p.get_height() == 1 for p in fig.axes[0].patches)
    assert all(p.get_x() == 0 for p in fig.axes[0].patches)
    assert all(p.get_y() == i for i, p in enumerate(fig.axes[0].patches))
    assert all(p.get_width() == 1 for p in fig.axes[0].patches)
    assert all(p.get_facecolor() == (0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 1.0) for p in fig.axes[0].patches)
    assert all(p.get_edgecolor() == (0.0, 0.0, 0.0, 1.0) for p in fig.axes[0].patches)
    assert all(p.get_linewidth() == 0.5 for p in fig.axes[0].patches)
    assert all(p.get_label() == f'Label{i + 1}' for i, p in enumerate(fig.axes[0].patches))
    assert all(p.get_visible() for p in fig.axes[0].patches)
    assert all(isinstance(t, plt.Text) for t in fig.axes[0].texts)
    assert all(t.get_text() == f'{p.get_height():.2f}' for p, t in zip(fig.axes[0].patches, fig.axes[0].texts))
    assert all(t.get_position() == (p.get_x() + p.get_width() / 2, p.get_y() + p.get_height() / 2) for p, t in zip(fig.axes[0].patches, fig.axes[0].texts))
    assert all(t.get_color() == (0.0, 0.0, 0.0, 1.0) for t in fig.axes[0].texts)
    assert all(t.get_fontsize() == 10 for t in fig.axes[0].texts)
    assert all(t.get_fontweight() == 'bold' for t in fig.axes[0].texts)
    assert all(t.get_ha() == 'center' for t in fig.axes[0].texts)
    assert all(t.get_va() == 'center' for t in fig.axes[0].texts)
    assert all(t.get_visible() for t in fig.axes[0].texts)
    assert all(isinstance(l, plt.legend.Legend) for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(isinstance(t, str) for t in fig.axes[0].get_legend_handles_labels()[1])
    assert all(t == f'Label{i + 1}' for i, t in enumerate(fig.axes[0].get_legend_handles_labels()[1]))
    assert all(l.get_visible() for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_frame_on() for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_frame_alpha() == 1.0 for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_facecolor() == (1.0, 1.0, 1.0, 1.0) for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_edgecolor() == (0.0, 0.0, 0.0, 1.0) for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_fancybox() for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_shadow() for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_ncol() == 1 for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_bbox_to_anchor() == (0.5, 1.0) for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(l.get_loc() == 'center left' for l in fig.axes[0].get_legend_handles_labels()[0])
    assert all(isinstance(t, plt.Text) for t in fig.texts)
    assert all(t.get_text() == f'Label{i + 1}' for i, t in enumerate(fig.texts))
    assert all(t.get_position() == (0.5, 0.95 - i * 0.05) for i, t in enumerate(fig.texts))
    assert all(t.get_color() == (0.0, 0.0, 0.0, 1.0) for t in fig.texts)
    assert all(t.get_fontsize() == 16 for t in fig.texts)
    assert all(t.get_fontweight() == 'bold' for t in fig.texts)
    assert all(t.get_ha() == 'center' for t in fig.texts)
    assert all(t.get_va() == 'center' for t in fig.texts)
    assert all(t.get_visible() for t in fig.texts)
    assert all(isinstance(l, plt.legend.Legend) for l in fig.get_legend_handles_labels()[0])
    assert all(isinstance(t, str) for t in fig.get_legend_handles_labels()[1])
    assert all(t == f'Label{i + 1}' for i, t in enumerate(fig.get_legend_handles_labels()[1]))
    assert all(l.get_visible() for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_frame_on() for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_frame_alpha() == 1.0 for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_facecolor() == (1.0, 1.0, 1.0, 1.0) for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_edgecolor() == (0.0, 0.0, 0.0, 1.0) for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_fancybox() for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_shadow() for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_ncol() == 1 for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_bbox_to_anchor() == (0.5, 1.0) for l in fig.get_legend_handles_labels()[0])
    assert all(l.get_loc() == 'center left' for l in fig.get_legend_handles_labels()[0])