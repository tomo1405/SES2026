python
import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import pytest

def task_func(num_types=5, integer_range=(0, 100)):
    LABELS = [f'Type{i + 1}' for i in range(num_types)]
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in LABELS})

    fig, ax = plt.subplots()
    data.plot(kind='barh', stacked=True, ax=ax)

    return fig, ax

def test_task_func():
    fig, ax = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.patches) == 5
    assert all(isinstance(p, plt.Rectangle) for p in ax.patches)
    assert all(p.get_height() == 100 for p in ax.patches)
    assert all(p.get_width() == 100 for p in ax.patches)
    assert all(p.get_x() == 0 for p in ax.patches)
    assert all(p.get_y() == i * 100 for i, p in enumerate(ax.patches))
    assert all(p.get_facecolor() == (0, 0, 0, 0) for p in ax.patches)
    assert all(p.get_edgecolor() == (0, 0, 0, 1) for p in ax.patches)
    assert all(p.get_label() == f'Type{i + 1}' for i, p in enumerate(ax.patches))
    assert all(p.get_alpha() == 1 for p in ax.patches)
    assert all(p.get_visible() for p in ax.patches)
    assert all(isinstance(t, plt.Text) for t in ax.texts)
    assert all(t.get_text() == f'{randint(*integer_range)}' for t in ax.texts)
    assert all(t.get_position() == (50, i * 100 + 50) for i, t in enumerate(ax.texts))
    assert all(t.get_color() == (0, 0, 0, 1) for t in ax.texts)
    assert all(t.get_fontsize() == 12 for t in ax.texts)
    assert all(t.get_fontweight() == 'bold' for t in ax.texts)
    assert all(t.get_ha() == 'center' for t in ax.texts)
    assert all(t.get_va() == 'center' for t in ax.texts)
    assert all(t.get_visible() for t in ax.texts)
    assert all(isinstance(l, plt.legend.Legend) for l in ax.get_legend_handles_labels()[0])
    assert all(isinstance(t, str) for t in ax.get_legend_handles_labels()[1])
    assert all(l.get_label() == t for l, t in zip(ax.get_legend_handles_labels()[0], ax.get_legend_handles_labels()[1]))
    assert all(l.get_alpha() == 1 for l in ax.get_legend_handles_labels()[0])
    assert all(l.get_visible() for l in ax.get_legend_handles_labels()[0])
    assert all(isinstance(t, plt.Text) for t in ax.get_legend().get_texts())
    assert all(t.get_text() == f'{randint(*integer_range)}' for t in ax.get_legend().get_texts())
    assert all(t.get_color() == (0, 0, 0, 1) for t in ax.get_legend().get_texts())
    assert all(t.get_fontsize() == 12 for t in ax.get_legend().get_texts())
    assert all(t.get_fontweight() == 'bold' for t in ax.get_legend().get_texts())
    assert all(t.get_ha() == 'center' for t in ax.get_legend().get_texts())
    assert all(t.get_va() == 'center' for t in ax.get_legend().get_texts())
    assert all(t.get_visible() for t in ax.get_legend().get_texts())
    assert all(isinstance(l, plt.Line2D) for l in ax.get_legend().get_lines())
    assert all(l.get_color() == (0, 0, 0, 1) for l in ax.get_legend().get_lines())
    assert all(l.get_linewidth() == 1 for l in ax.get_legend().get_lines())
    assert all(l.get_visible() for l in ax.get_legend().get_lines())
    assert all(isinstance(t, plt.Text) for t in ax.get_title().get_text())
    assert ax.get_title().get_text() == ''
    assert ax.get_xlabel() == ''
    assert ax.get_ylabel() == ''
    assert ax.get_xlim() == (0, 500)
    assert ax.get_ylim() == (-50, 450)
    assert ax.get_xticks() == []
    assert ax.get_yticks() == []
    assert ax.get_xticklabels() == []
    assert ax.get_yticklabels() == []
    assert ax.get_frame_on() == True
    assert ax.get_facecolor() == (1, 1, 1, 0)
    assert ax.get_edgecolor() == (0, 0, 0, 1)
    assert ax.get_navigate() == True
    assert ax.get_aspect() == 'auto'
    assert ax.get_autoscale_on() == True
    assert ax.get_xmargin() == 0.05
    assert ax.get_ymargin() == 0.05
    assert ax.get_navigate() == True
    assert ax.get_navigate_mode() == 'PAN_ZOOM'
    assert ax.get_picker() == True
    assert ax.get_snap() == True
    assert ax.get_gid() == ''
    assert ax.get_label() == ''
    assert ax.get_animated() == False
    assert ax.get_zorder() == 1
    assert ax.get_navigate() == True
    assert ax.get_navigate_mode() == 'PAN_ZOOM'
    assert ax.get_picker() == True
    assert ax.get_snap() == True
    assert ax.get_gid() == ''
    assert ax.get_label() == ''
    assert ax.get_animated() == False
    assert ax.get_zorder() == 1